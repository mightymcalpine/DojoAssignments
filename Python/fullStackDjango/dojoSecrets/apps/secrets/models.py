# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logReg.models import UserDB

class SecretDBChief(models.Manager):
	def postSecret(self, currentUser, postData):
		errors = []
		if len(postData['newSecret']) < 2:
			errors.append(['newSecret', 'oops your secret cannot be less than 2 characters'])
		if errors:
			return [False, errors]
		else:
			newSecret = SecretDB(secret = postData['newSecret'], author = currentUser)
			# ****** CHECK DATA SECTION *******
			print '*'*50
			print newSecret.secret
			print '*'*50
			# ****** END CHECK *******
			return [True, newSecret]
	
# UserDB in LogReg models.py

class SecretDB(models.Model):
	secret = models.TextField(default=None)
	author = models.ForeignKey(UserDB, related_name="authorSecret", on_delete=models.CASCADE)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	
	objects = SecretDBChief()
	
	def __str__(self):
		return 'newSecret author: %s' % (self.author)
	
class LikeDB(models.Model):
	author = models.ForeignKey(UserDB, related_name="authorLike", on_delete=models.CASCADE)
	secret = models.ForeignKey(SecretDB, related_name="secretLike", on_delete=models.CASCADE)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	