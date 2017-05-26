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
			# could place user in session
			messages.success(request, 'The username you entered ' + response[1].username + ' is valid. Thank You.')
			# confirm good user go here
			return redirect('validateUser:dashBoard')
	# not a POST, redirect
	return redirect('validateUser:index')

def dashBoard(request):
	context = {
		'users': UserDB.objects.all()
	}
	return render(request, 'validateUser/dashBoard.html', context)
	
# ***** ORIGINAL CODE *****
# def confirmDelete(request, id):
# 	# get whole object of passed in id
# 	request.session['id'] = id
# 	return redirect('validateUser:dashBoard')

# ********* TESTING AREA ***************
# OPTION-1
# def confirmDelete(request, id):
# 	context = {
# 		'bacon': UserDB.objects.filter(id=id)
# 	}
# 	print 'HERE ', context['bacon']
# 	request.session['id'] = id
# 	return render(request, 'validateUser/dashBoard.html', context)

# OPTION-2
def confirmDelete(request, id):
	# get whole object of passed in id
	request.session['id'] = id
	request.session['username'] = UserDB.objects.filter(id=id)
	
	return redirect('validateUser:dashBoard')

# ********* TESTING AREA ***************



def delete(request, id):
	if request.method == 'POST':
		if request.POST['delete'] == 'yes':
			UserDB.objects.get(id=id).delete()
			request.session.clear()
			return redirect('validateUser:dashBoard')
		elif request.POST['delete'] == 'no':
			request.session.clear()
			return redirect('validateUser:dashBoard')
	else:
		return redirect('validateUser:dashBoard')