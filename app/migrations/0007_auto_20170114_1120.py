# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170114_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='months',
        ),
        migrations.AddField(
            model_name='month',
            name='Employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Employee'),
            preserve_default=False,
        ),
    ]
