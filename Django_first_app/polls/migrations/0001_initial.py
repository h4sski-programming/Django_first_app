# Generated by Django 4.1.3 on 2022-11-07 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('email', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vechicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('total_distance', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user_vechicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('distance', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
                ('vechicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vechicle')),
            ],
        ),
    ]
