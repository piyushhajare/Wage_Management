# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20170123_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
