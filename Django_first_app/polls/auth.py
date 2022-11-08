from django.shortcuts import render
from django import forms

from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=200)
    password = forms.PasswordInput()


def login(request):
    users = User.objects.all()
    form = LoginForm()
    return render(request, 'polls/registration/login.html',
                  {'users': users, 'form': form})
