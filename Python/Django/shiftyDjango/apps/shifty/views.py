# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	return render(request, 'shifty/index.html')

def show(request):
	print request.method
	return render(request, 'shifty/showUsers.html')
