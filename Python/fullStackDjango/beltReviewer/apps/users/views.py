# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import UsersDB

# Create your views here.
def index(request):
	# if 'user' in request.session:
	# 	pass
	# 	# set context
	# 	return render(request, 'users/index.html')
	# return redirect('users:index')
	return render(request, 'users/index.html')

def logReg(request):
	if request.method == 'POST':
		if request.POST['users'] == 'register':
			response = UsersDB.objects.validateReg(request.POST)
		elif request.POST['users'] == 'login':
			response = UsersDB.objects.validateLogin(request.POST)
		if not response[0]:
			for message in response[1]:
				messages.error(request, message[1])
			return redirect('users:index')
		else:
			request.session['user'] = {
				'id': response[1].id,
				'firstName': response[1].firstName,
				'lastName': response[1].lastName
			}
			return redirect('books:home')
	return redirect(request, 'users:index')

def logout(request):
	request.session.clear()
	return redirect('users:index')
		
	

	