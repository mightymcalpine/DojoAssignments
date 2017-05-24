# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
	first_name = models.CharField(max_length = 92)
	last_name = models.CharField(max_length = 92)
	email = models.CharField(max_length = 128)
	password = models.CharField(max_length = 64)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Messages(models.Model):
	user_id = models.ForeignKey(Users)
	message = models.TextField()	
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Comments(models.Model):
	message_id = models.ForeignKey(Messages)
	user_id = models.ForeignKey(Users)
	comments = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	