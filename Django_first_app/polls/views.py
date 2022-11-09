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
    return render(request, 'polls/profile.html',
                  {'u': user, 'vehicles': vehicles})


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
    calendar_day = first_day_first_week

    calendar_list_days = []

    for i in range(5):
        week_list = []
        for j in range(7):
            if not calendar_list_days:
                week_list = [int(calendar_day.day)]
                continue
            calendar_day = calendar_day + timedelta(days=1)
            week_list.append(int(calendar_day.day))
        week_list.append('')
        calendar_list_days.append(week_list)

    return render(response, 'polls/calendar.html', {
        'today': today,
        'first_month_day': first_month_day,
        'first_day_first_week': first_day_first_week,
        'calendar_list_days': calendar_list_days,
        })
