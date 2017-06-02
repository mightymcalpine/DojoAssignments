# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
# regex capture for username
USERREG = re.compile(r'^[a-zA-Z0-9_-]\S{8,16}$')

class UserDBChief(models.Manager):
	def validateCreate(self, postData):
		# a list of lists
		errors = []
		# check if username from postData passes regex string
		if not re.match(USERREG, postData['username']):
		# if len(postData['username']) < 9:
			# append a list to the errors list
		 	errors.append(['username', 'username must be between 8-16 characters, with no spaces, - or _ is acceptable'])
		if errors:
		 	# send a list back to controller 
		 	return [False, errors]
		else:
		 	# is the username from postDate already in the DB
		 	existingUser = UserDB.objects.filter(username=postData['username'])
		 	# if it is, append an error to the list of errors
		 	if existingUser:
		 		errors.append(['existingUser', 'The username you entered already exists, please try a different username'])
		 		return [False, errors]
		 	# create new user with postData
		 	newUser = UserDB(username = postData['username'])
		 	# insert into DB
		 	newUser.save()
		 	# view newUser object in str version from __str__ method
		 	print newUser
		 	# send list back to controller which has our newUser
		 	return [True, newUser]


class UserDB(models.Model):
	username = models.CharField(max_length = 64)
	createdDate = models.DateField(auto_now_add = True)
	createdTime = models.TimeField(auto_now_add = True)
	
	objects = UserDBChief()
	
	# method for viewing object from DB
	def __str__(self):
		return 'ID: %s | Username: %s | Date: %s | Time: %s' % (self.id, self.username, self.createdDate, self.createdTime)