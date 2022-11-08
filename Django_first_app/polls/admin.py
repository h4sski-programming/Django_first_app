from django.contrib import admin

from .models import User, Vehicle, Activity

# Register your models here.

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Activity)