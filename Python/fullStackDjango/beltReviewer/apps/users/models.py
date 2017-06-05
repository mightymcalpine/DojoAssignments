# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re, bcrypt

# Regex captures
nameREG = re.compile(r'^[a-zA-Z-]\S{2,64}$')
emailREG = re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')
pwREG = re.compile(r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{7,})\S$')

# users manager
class UsersDBManager(models.Manager):
	def encryptPW(self, password):
		return bcrypt.hashpw(password, bcrypt.gensalt())
	
	def validateReg(self, postData):
		errors = []
		if not re.match(nameREG, postData['firstName']):
			errors.append(['firstName', 'First Name must be at least 2 characters'])
		if not re.match(nameREG, postData['lastName']):
			errors.append(['lastName', 'Last Name must be at least 2 characters'])
		if not re.match(emailREG, postData['email']):
			errors.append(['email', 'Please enter a valid email address'])
		if not re.match(pwREG, postData['password']):
			errors.append(['password', 'password must have at least 8 characters, 1 lowercase letter, 1 uppercase letter, and a number'])
		if not postData['pwConfirm'] == postData['password']:
			errors.append(['pwConfirm', "oops you're passwords do not match"])
		if errors:
			return [False, errors]
		else:
			existingUser = UsersDB.objects.filter(email=postData['email'])
			if existingUser:
				errors.append(['existingUser', 'The email you entered is already registered. Please try a different email'])
				return [False, errors]
			else:
				newUser = UsersDB.objects.create(firstName = postData['firstName'], lastName = postData['lastName'], email = postData['email'])
				newUser.password = self.encryptPW(postData['password'].encode())
				newUser.save()
			return [True, newUser]

	def validateLogin(self, postData):
		errors = []
		if not re.match(emailREG, postData['email']) or len(postData['password']) < 8:
			errors.append(['email', 'The email or password is incorrect'])
			return [False, errors]
		try:
			existingUser = UsersDB.objects.get(email=postData['email'])
		except:
			errors.append(['email', 'The email or password is incorrect'])
			return [False, errors]
		
		if not existingUser:
			errors.append(['existingUser', 'the email or password you entered is incorrect'])
		if bcrypt.hashpw(postData['password'].encode(), existingUser.password.encode()) != existingUser.password:
			errors.append(['existingUser', 'the email or password you entered is incorrect'])
		if errors:
			return [False, errors]
		else:
			return [True, existingUser]

# users model
class UsersDB(models.Model):
	firstName = models.CharField(max_length = 64)
	lastName = models.CharField(max_length = 64)
	email = models.CharField(max_length = 128)
	password = models.CharField(max_length = 255)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	objects = UsersDBManager()
	
	# method for viewing user objects
	def __str__(self):
		return 'ID: %s | FirstName: %s | LastName: %s | Email: %s' % (self.id, self.firstName, self.lastName, self.email)