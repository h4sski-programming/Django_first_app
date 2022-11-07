from django.shortcuts import render

from .models import User, Vechicle, Activity


# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, 'polls/index.html', {'users': users})


def profile(request):
    user = User.objects.get(id=1)
    user_vechicles = Vechicle.objects.filter(user_vechicle=user.id)
    return render(request, 'polls/profile.html', {'u': user, 'vechicles': user_vechicles})


def add_vechicle(request):
    return render(request, f'polls/')