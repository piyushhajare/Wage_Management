# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('no_of_holidays', models.CharField(max_length=10)),
                ('total_advance_overhead', models.CharField(max_length=15)),
            ],
        ),
    ]
