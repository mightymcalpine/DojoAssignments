# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from ..users.models import UsersDB

class BooksDBManager(models.Manager):
	def createBookReview(self, postData, id):
		errors = []
		user = UsersDB.objects.get(id=id)
		existingBook = BooksDB.objects.filter(title=postData['title'])
		if existingBook:
			errors.append(['exisitingBook', 'This Book has already been added'])
		if len(postData['title']) < 2:
			errors.append(['title', 'Title must be longer than 2 characters'])
		if len(postData['review']) < 4:
			errors.append(['review', 'Review must be longer than 2 characters'])
		if postData['authorSelect'] == 'select':
			if len(postData['authorInput']) < 2:
				errors.append(['authorSelect', 'Author name must be longer than 2 characters'])
			else:
				newAuthor = AuthorsDB.objects.create(name = postData['authorInput'])
				author = AuthorsDB.objects.get(name = postData['authorInput'])
		else:
			author = AuthorsDB.objects.get(name = postData['authorSelect'])
		if errors:
			return [False, errors]
		else:
			newBook = BooksDB.objects.create(title = postData['title'], author = author)
			newReview = ReviewsDB.object.create(review = postData['review'], rating = postData['stars'], user = user, book = BooksDB.objects.get(title = postData['title']))
			return [True, newBook]
			
			

class AuthorsDBManager(models.Manager):
	pass

class ReviewsDBManager(models.Manager):
	def createReview(self, postData, user, book):
		errors = []
		if len(postData['review']) < 4:
			errors.append(['review', 'Your review must be at least 4 characters long'])
		if errors:
			return [False, errors]
		else:
			newReview = ReviewsDB.objects.create(review = postData['review'], rating = postData['stars'], user = user, book = book)
			return True

class AuthorsDB(models.Model):
	name = models.CharField(max_length=92)
	# may not need user in each table
	user = models.ForeignKey(UsersDB, related_name="usersAuthors")
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)
	objects = AuthorsDBManager()
	
	
class BooksDB(models.Model):
	title = models.CharField(max_length=255)
	# the authors books, one author has many books
	author = models.ForeignKey(AuthorsDB, related_name="authorsBooks")
	user = models.ForeignKey(UsersDB, related_name="usersBooks")
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)
	objects = BooksDBManager()


class ReviewsDB(models.Model):
	user = models.ForeignKey(UsersDB, related_name="usersReviews") 
	book = models.ForeignKey(BooksDB, related_name="booksReviews")
	review = models.TextField()
	rating = models.IntegerField()
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now=True)
	objects = ReviewsDBManager()
