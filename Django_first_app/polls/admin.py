from django.contrib import admin

from .models import User, Vechicle, Activity

# Register your models here.

admin.site.register(User)
admin.site.register(Vechicle)
admin.site.register(Activity)