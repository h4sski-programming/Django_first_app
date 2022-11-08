from django.shortcuts import render

from .forms.add_vechicle import AddVechicleForm
from .models import User, Vechicle, Activity


def index(request):
    users = User.objects.all()
    return render(request, 'polls/index.html', {'users': users})


def profile(request, user_id):
    user = User.objects.get(id=user_id)
    user_vechicles = Vechicle.objects.filter(user_vechicle=user.id)
    return render(request, 'polls/profile.html',
                  {'u': user, 'vechicles': user_vechicles})


def add_vechicle(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = AddVechicleForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            new_vechicle = Vechicle()
            new_vechicle.user_vechicle = user
            new_vechicle.name = name
            new_vechicle.type = type
            new_vechicle.save()
            return render(request, f'polls/add_vechicle.html',
                  {'form': form, 'v': new_vechicle})
    else:
        form = AddVechicleForm()
    return render(request, f'polls/add_vechicle.html',
                  {'form': form})
