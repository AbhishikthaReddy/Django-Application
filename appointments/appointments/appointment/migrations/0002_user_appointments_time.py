# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_appointments',
            name='time',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
