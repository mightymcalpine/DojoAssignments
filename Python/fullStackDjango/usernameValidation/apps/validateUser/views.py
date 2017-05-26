# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import UserDB

def index(request):
	return render(request, 'validateUser/index.html')

def addUser(request):
	# check the type of HTTP request from template form
	if request.method == 'POST':
		# send form data to models for val and create
		# validateCreate method from models returns a list
		response = UserDB.objects.validateCreate(request.POST)
		# the element at response[0] is False
		if not response[0]:
			# element at response[1] is the list of errors
			for message in response[1]:
				messages.error(request, message[1])
			return redirect('validateUser:index')
		else:
			# could place user in session here
			messages.success(request, 'The username you entered ' + response[1].username + ' is valid. Thank You.')
			# confirm good user go here
			return redirect('validateUser:dashBoard')
	# not a POST, redirect
	return redirect('validateUser:index')

def dashBoard(request):
	# query all users for displaying in template
	context = {
		'users': UserDB.objects.all()
	}
	return render(request, 'validateUser/dashBoard.html', context)

def confirmDelete(request, id):
	# place specified id in session
	request.session['id'] = id
	# query for all users for diplay and user of specified id
	context = {
		'users': UserDB.objects.all(),
		'thisUser': UserDB.objects.filter(id=id).get(id=id)
	}
	return render(request, 'validateUser/dashBoard.html', context)

def delete(request, id):
	if request.method == 'POST':
		# clicked yes delete button, delete user, clear session
		if request.POST['delete'] == 'yes':
			UserDB.objects.get(id=id).delete()
			request.session.clear()
			return redirect('validateUser:dashBoard')
		# clicked button to not delete, clear session, redirect 
		elif request.POST['delete'] == 'no':
			request.session.clear()
			return redirect('validateUser:dashBoard')
	else:
		return redirect('validateUser:dashBoard')