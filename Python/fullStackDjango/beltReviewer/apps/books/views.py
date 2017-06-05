# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import UsersDB, AuthorsDB, BooksDB, ReviewsDB 

# books app Controllers

def home(request):
	if 'user' in request.session:
		pass
		return render(request, 'books/home.html')
	return redirect('users:index')

def newBook(request, id):
	context = {
		'id': id,
		'book': BooksDB.objects.get(id=id),
		'user': UsersDB.objects.get(id=request.session['user']['id'])
	}
	return render(request, 'books/addbook.html', context)

def userProfile(request):
	# pass user Id
	pass
	return render(request, 'books/userprofile.html')

def bookProfile(request):
	context = {
		'allReviews': ReviewsDB.objects.all()
	}
	return render(request, 'books/bookprofile.html', context)

# 	*** may be possible to combine addReviewBook and ReviewBook into one
def addBookReview(request):
	if request.method == 'POST':
		response = BooksDB.objects.createBookReview(request.POST, request.session['user']['id'])
		if not response[0]:
			for message in response[1]:
				messages.error(request, message[1])
			return redirect('books:newBook')
		else:
			return redirect('books:bookProfile', id=response[1].id)
	return redirect('books:bookProfile')


def addReview(request, id):
	if request.method == 'POST':
		user = UsersDB.objects.get(id=request.session['user']['id'])
		book = BooksDB.objects.get(id=id)
		response = ReviewsDB.objects.createReview(request.POST, user, book)
		if not response[0]:
			for message in response[1]:
				message.error(request, message[1])
			return redirect('books:bookProfile')
		else:
			return redirect('books:bookProfile')
	return redirect('books:bookProfile')


def deleteBook(request, id):
	ReviewsDB.objects.filter(id=id).delete()
	return redirect('books:bookProfile')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
