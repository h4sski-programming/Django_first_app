# Generated by Django 4.1.3 on 2022-11-08 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_vechicle_create_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vechicle',
            old_name='user_vechicle',
            new_name='user',
        ),
    ]
