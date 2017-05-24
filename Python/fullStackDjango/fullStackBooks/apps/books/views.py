# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import bookDB, bookDBManager
# import re

def index(request):
	allBooks = bookDB.objects.all()
	context = {
		'books': allBooks,
	}	
	return render(request, 'books/index.html', context)

def addBook(request):
	if request.method == 'POST':
		bookDB.objects.validateAndCreate(request.POST)
	return redirect('/')

def delete(request, id):
	bookDB.objects.get(id=id).delete()
	return redirect('/')