from django.shortcuts import render

from .models import User


# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, 'polls/index.html', {'users': users})

def profile(request):
    user = User.objects.get(id=1)
    return render(request, 'polls/profile.html', {'u': user})