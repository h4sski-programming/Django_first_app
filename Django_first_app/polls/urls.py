from django.urls import path

from . import views, auth

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.profile, name='profile'),
    path('<int:user_id>/add_vechicle/', views.add_vechicle, name='add_vechicle'),
    path('login/', auth.login, name='login'),
    ]
