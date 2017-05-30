# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import UserDB

def index(request):
	return render(request, 'logReg/index.html')

def process(request):
	if request.method == 'POST':
		if request.POST['logReg'] == 'register':
			response = UserDB.objects.validateReg(request.POST)
		elif request.POST['logReg'] == 'login':
			response = UserDB.objects.validateLog(request.POST)
		if not response[0]:
			for message in response[1]:
				messages.error(request, message[1])
			return redirect('logReg:index')
		else:
			request.session['user'] = {
				'id': response[1].id,
				'firstName': response[1].firstName,
				'lastName': response[1].lastName
			}
			messages.success(request, 'Success! Welcome ' + response[1].firstName)
			return redirect('logReg:success')
	return redirect('logReg:index')

def success(request):
	if 'user' not in request.session:
		return redirect('logReg:index')
	context = {
		'users': UserDB.objects.all()
	}	
	return render(request, 'logReg/success.html', context)

def logout(request):
	if request.method == 'GET':
		request.session.clear()
		return redirect('logReg:index')