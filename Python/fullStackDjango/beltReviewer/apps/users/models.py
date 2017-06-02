# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models

# users manager
class UserDBManager(models.Manager):
	def validateCreate(self, postData):
		pass

# users model
class UserDB(models.Model):
	firstName = models.CharField(max_length = 64)
	lastName = models.CharField(max_length = 64)
	email = models.CharField(max_length = 128)
	pwHash = models.CharField(max_length = 255)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	objects = UserDBManager()
	
	# method for viewing user objects
	def __str__(self):
		return 'ID: %s | FirstName: %s | LastName: %s | Email: %s' % (self.id, self.firstName, self.lastName, self.email)