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
            vehicle.name = response.POST.get('name')
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
