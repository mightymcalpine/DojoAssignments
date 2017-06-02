# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import UserDB

# Create your views here.
def index(request):
	pass
	return render(request, 'users:index.html')

def logReg(request):
	pass
	# if post == reg
		# go here models
	# if post == login
		# go here models
	# response (var) from models
	# bad reg or login
	# messages
	return redirect(request, 'users:index')
	
	# good reg or login
	return redirect(request, 'books:home')

def logout(request):
	pass
	# clear session
	return redirect(request, 'users:index')

	