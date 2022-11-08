from django.shortcuts import render

from .forms_custom import AddVehicleForm
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
    else:
        form = AddVehicleForm()
    return render(request, f'polls/vehicle.html',
                  {'form': form, 'vehicles': vehicles, 'u': user})
