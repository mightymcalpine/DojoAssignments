# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import UserDB # books models

# books app Controllers

def home(request):
	if 'user' in request.session:
		pass
		return render(request, 'books:home.html')
	return redirect('users:index')

def addBook(request):
	pass
	return render(request, 'books:addbook.html')

def userProfile(request):
	pass
	return render(request, 'books:userprofile.html')

def bookProfile(request):
	# may need to pass in book ID
	pass
	return render(request, 'books:bookprofile.html')

# 	*** may be possible to combine addReviewBook and ReviewBook into one
def addReviewBook(request):
	# may need to pass in book ID
	pass
	return redirect('books:bookProfile')

def bookReview(request):
	# may need to pass in book ID
	pass
	return redirect('books:bookProfile')

def delete(request):
	pass
	return redirect('books:bookProfile')