# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170119_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='no_of_ot_hours',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]