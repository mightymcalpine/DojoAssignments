# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
	return render(request, 'landscapes/index.html')

def landscapes(request, num):
	number = int(num)
	context = {
		'num': number,
	}
	if number <= 10:
		context['img'] = 'landscapes/images/snow.jpg'
	elif number <= 20:		
		context['img'] = 'landscapes/images/desert.jpg'
	elif number <= 30:		
		context['img'] = 'landscapes/images/forest.jpg'
	elif number <= 40:		
		context['img'] = 'landscapes/images/vineyard.jpg'
	elif number <= 50:		
		context['img'] = 'landscapes/images/beach.jpg'
	else:
		messages.add_message(request, messages.INFO, "oops you entered " + num + " your number has to be less than 50.")
		return redirect('/')
	return render(request, 'landscapes/landscapes.html', context)