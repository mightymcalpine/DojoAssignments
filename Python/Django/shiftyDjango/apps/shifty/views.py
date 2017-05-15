# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.shortcuts import render

def index(request):
	return render(request, 'shifty/index.html')

def show(request):
	print request.method
	return render(request, 'shifty/showUsers.html')

def addUser(request):
	if request.method == 'POST':
		print '*'*50
		print 'METHOD:', request.method
		# returns the method/HTTP verb assoc with request
		print request.POST
		# data from POST request, dictionary 
		print '*'*50
		request.session['user'] = {
			'name': request.POST['fname']
		}
		# request.session['name'] = request.POST['fname']
		return redirect('/')
	else:
		return redirect('/')

