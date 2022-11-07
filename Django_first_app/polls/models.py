from django.db import models


# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_created=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vechicle(models.Model):
    user_vechicle = models.ForeignKey(User, on_delete=models.CASCADE)
    total_distance = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_created=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.type}'


class Activity(models.Model):
    user_activity = models.ForeignKey(User, on_delete=models.CASCADE)
    distance = models.IntegerField()
    type = models.CharField(max_length=50)
    vechicle = models.ForeignKey(Vechicle, on_delete=models.CASCADE)
    date = models.DateField()
    create_time = models.DateTimeField(auto_created=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.distance} | {self.type} | {self.date}'
