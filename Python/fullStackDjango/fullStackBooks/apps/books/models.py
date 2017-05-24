# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class bookDBManager(models.Manager):
	def validateAndCreate(self, data):
		newBook = bookDB(title = data['title'], author = data['author'], category = data['category'])
		newBook.save()

class bookDB(models.Model):
	title = models.CharField(max_length = 128)
	author = models.CharField(max_length = 64)
	category = models.CharField(max_length = 64)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	objects = bookDBManager()
	