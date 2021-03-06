# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='sticker_admin', max_length=130, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(default='varnish', max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validation_app.Acl')),
                ('feature_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validation_app.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='ban_request', max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validation_app.Acl')),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='validation_app.Task'),
        ),
    ]
