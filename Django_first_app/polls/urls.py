from django.urls import path

from . import views, auth

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.profile, name='profile'),
    path('<int:user_id>/vehicle/', views.vehicle, name='vehicle'),
    path('login/', auth.login, name='login'),
    ]
