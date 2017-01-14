# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170114_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='month',
            name='employees',
        ),
        migrations.AddField(
            model_name='employee',
            name='months',
            field=models.ManyToManyField(to='app.Month'),
        ),
    ]