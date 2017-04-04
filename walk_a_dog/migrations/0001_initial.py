# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 08:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='/static/')),
                ('name', models.CharField(max_length=64)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female')])),
                ('year_of_birth', models.IntegerField()),
                ('breed', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voivodeship', models.IntegerField(choices=[(1, 'woj. dolnośląskie'), (2, 'woj. kujawsko-pomorskie'), (3, 'woj. lubelskie'), (4, 'woj. lubuskie'), (5, 'woj. łódzkie'), (6, 'woj. małopolskie'), (7, 'woj. mazowieckie'), (8, 'woj. opolskie'), (9, 'woj. podkarpackie'), (10, 'woj. podlaskie'), (11, 'woj. pomorskie'), (12, 'woj. śląskie'), (13, 'woj. świętokrzyskie'), (14, 'woj. warmińsko-mazurskie'), (15, 'woj. wielkopolskie'), (16, 'woj. zachodniopomorskie')])),
                ('city', models.CharField(max_length=64)),
                ('fav_walking_place', models.TextField()),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voivodeship', models.IntegerField(choices=[(1, 'woj. dolnośląskie'), (2, 'woj. kujawsko-pomorskie'), (3, 'woj. lubelskie'), (4, 'woj. lubuskie'), (5, 'woj. łódzkie'), (6, 'woj. małopolskie'), (7, 'woj. mazowieckie'), (8, 'woj. opolskie'), (9, 'woj. podkarpackie'), (10, 'woj. podlaskie'), (11, 'woj. pomorskie'), (12, 'woj. śląskie'), (13, 'woj. świętokrzyskie'), (14, 'woj. warmińsko-mazurskie'), (15, 'woj. wielkopolskie'), (16, 'woj. zachodniopomorskie')])),
                ('city', models.CharField(max_length=64)),
                ('date_start', models.DateTimeField()),
                ('date_stop', models.DateTimeField()),
                ('dog', models.ManyToManyField(to='walk_a_dog.Dog')),
            ],
        ),
    ]
