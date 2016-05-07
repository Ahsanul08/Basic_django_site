from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Acl(models.Model):
    category = models.CharField( max_length=130, default= 'sticker_admin', unique = True)

class User(models.Model):
    acl_id = models.ForeignKey(Acl)
    user_name = models.CharField( max_length= 100, default= 'cloud', unique= True)
    password = models.CharField( max_length= 100, default= '123456')

class Feature(models.Model):
    feature_name = models.CharField( max_length= 60, default= 'varnish', unique= True)

class Task(models.Model):
    task_name = models.CharField( max_length= 60, default= 'ban_request', unique= True)

class Role(models.Model):
    acl_id = models.ForeignKey(Acl)
    feature_id = models.ForeignKey(Feature)
    task_id = models.ForeignKey(Task)