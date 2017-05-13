# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	print "Secret Weapon"
	return render(request, 'portfolio/index.html')

def testimonials(request):
	print 'Method:', request.method
	return render(request, 'portfolio/testimonials.html')