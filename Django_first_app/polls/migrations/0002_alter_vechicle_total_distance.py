# Generated by Django 4.1.3 on 2022-11-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vechicle',
            name='total_distance',
            field=models.IntegerField(default=0),
        ),
    ]
