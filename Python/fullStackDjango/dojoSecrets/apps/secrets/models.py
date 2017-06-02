# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
from ..logReg.models import UserDB
	
# UserDB in LogReg models.py 

# Secrets Chief
class SecretDBChief(models.Manager):
	def postSecret(self, currentUser, postData):
		errors = []
		if len(postData['newSecret']) < 2:
			errors.append(['newSecret', 'oops your secret cannot be less than 2 characters'])
		if errors:
			return [False, errors]
		else:
			newSecret = SecretDB.objects.create(secret = postData['newSecret'], author = currentUser)
			# newSecret.save()
			return [True, newSecret]

# Secrets DB
class SecretDB(models.Model):
	secret = models.TextField(default=None)
	author = models.ForeignKey(UserDB, related_name="authorSecret", on_delete=models.CASCADE)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def getLikeAuthor(self):
		return UserDB.objects.filter(authorLike__secret=self)
	objects = SecretDBChief()
	
	def __str__(self):
		return 'Secret: %s | Author: %s' % (self.secret, self.author)

# Likes Chief
class LikeDBChief(models.Manager):
	def likeSecret(self, secretID, authorID):
		# create newLike with author and specified secret
		newLike = LikeDB.objects.create(author = authorID, secret = secretID)
		# return newLike
		

# Likes DB
class LikeDB(models.Model):
	author = models.ForeignKey(UserDB, related_name="authorLike", on_delete=models.CASCADE)
	secret = models.ForeignKey(SecretDB, related_name="secretLike", on_delete=models.CASCADE)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	
	objects = LikeDBChief()
















	