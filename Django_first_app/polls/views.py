from datetime import date, timedelta

from django.shortcuts import render, redirect

from .forms_custom import AddVehicleForm, VehicleChoiceForm
from .models import User, Vehicle, Activity


def index(request):
    users = User.objects.all()
    vehicles = Vehicle.objects.all()
    activitys = Activity.objects.all()
    return render(request, 'polls/index.html',
                  {'users': users, 'vehicles': vehicles, 'activitys': activitys})


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    vehicles = Vehicle.objects.filter(user=user.id)
    activities = Activity.objects.filter(user=user.id)
    return render(request, 'polls/profile.html', {
        'u': user,
        'vehicles': vehicles,
        'activities': activities,
        })


def vehicle(request, user_id):
    user = User.objects.get(id=user_id)
    vehicles = Vehicle.objects.filter(user=user_id)
    if request.method == 'POST':
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            new_vehicle = Vehicle()
            new_vehicle.user = user
            new_vehicle.name = name
            new_vehicle.type = type
            new_vehicle.save()
            return redirect(f'/{user_id}')
    else:
        form = AddVehicleForm()
        vehicle_form = VehicleChoiceForm()
    return render(request, f'polls/vehicle.html',
                  {'form': form,
                   'vehicles': vehicles,
                   'vehicle_form': vehicle_form,
                   'u': user,
                   })


def vehicle_edit(response, user_id, v_id):
    user = User.objects.get(id=user_id)
    vehicle = Vehicle.objects.get(id=v_id)
    if response.method == 'POST':
        if response.POST.get('edit'):
            new_name = response.POST.get('name')
            new_type = response.POST.get('type')
            if len(new_name) > 2:
                vehicle.name = new_name
            else:
                print('invalid new name of the vehicle')
            if new_type != vehicle.type:
                vehicle.type = new_type
            vehicle.save()
        elif response.POST.get('delete'):
            vehicle.delete()
        return redirect(f'/{user_id}/')
    vehicle_form = VehicleChoiceForm()
    return render(response, f'polls/vehicle_edit.html',
                  {'v': vehicle,
                   'vehicle_form': vehicle_form,
                   'u': user,
                   })


def calendar(response):
    today = date.today()
    first_month_day = today.replace(day=1)
    first_month_day_weekday = first_month_day.weekday()
    first_day_first_week = first_month_day - timedelta(days=first_month_day_weekday)

    temp_date = first_month_day
    calendar_list = []
    while today.month == temp_date.month:
        calendar_list.append(temp_date)
        temp_date = temp_date + timedelta(days=1)

    user = User.objects.get(id=1)
    activities_user = Activity.objects.filter(user=user)

    return render(response, 'polls/calendar.html', {
        'today': today,
        'calendar_list': calendar_list,
        'user': user,
        'activities_user': activities_user,
        })


def activity_edit(response):
    def convert_date(day_str):
        year, month, day_input = day_str.split('-')
        return date(int(year), int(month), int(day_input))

    user = User.objects.get(id=1)
    user_vehicles = Vehicle.objects.filter(user=user.id)

    if response.POST.get('save'):
        day = convert_date(response.POST.get('save'))
        distance = response.POST.get('distance')
        vehicle = Vehicle.objects.get(id=response.POST.get('vehicle_id'))
        new_activity = Activity()
        new_activity.user = user
        new_activity.vehicle = vehicle
        new_activity.distance = distance
        new_activity.date = day
        new_activity.save()
        return redirect(f'/{user.id}/')

    elif response.POST.get('day'):
        day = convert_date(response.POST.get('day'))
    else:
        print(f'Missing "save" or "day" input')

    vehicle_list = []
    for v in user_vehicles:
        vehicle_list.append(v)

    return render(response, 'polls/activity_edit.html', {
        'u': user,
        'day': day,
        'vehicle_list': vehicle_list,
        })
