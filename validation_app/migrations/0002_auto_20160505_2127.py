# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123456', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='cloud', max_length=100, unique=True),
        ),
    ]
