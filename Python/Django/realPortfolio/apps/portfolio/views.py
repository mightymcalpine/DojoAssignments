# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	print '#' * 50
	print 'Method Type:', request.method
	return render(request, 'portfolio/index.html')

def testimonials(request):
	return render(request, 'portfolio/testimonials.html')

def about(request):
	return render(request, 'portfolio/about.html')

def projects(request):
	return render(request, 'portfolio/projects.html')