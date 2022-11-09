from django.urls import path

from . import views, auth

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.profile, name='profile'),
    path('<int:user_id>/vehicle/', views.vehicle, name='vehicle'),
    path('<int:user_id>/vehicle/<int:v_id>', views.vehicle_edit, name='vehicle_edit'),
    path('calendar/', views.calendar, name='calendar'),
    path('login/', auth.login, name='login'),
    ]
