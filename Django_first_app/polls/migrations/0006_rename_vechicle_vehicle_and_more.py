# Generated by Django 4.1.3 on 2022-11-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_rename_user_activity_activity_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vechicle',
            new_name='Vehicle',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='vechicle',
            new_name='vehicle',
        ),
        migrations.AlterField(
            model_name='activity',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
