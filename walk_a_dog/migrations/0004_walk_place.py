# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk_a_dog', '0003_auto_20170405_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='walk',
            name='place',
            field=models.TextField(blank=True, null=True, verbose_name='Miejsce spaceru'),
        ),
    ]
