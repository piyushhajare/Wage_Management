# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20170124_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='month',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]