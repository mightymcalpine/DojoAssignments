# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'vanishingNinjas/index.html')

def ninjaColor(request, color):
	context = {
		'leo': 'vanishingNinjas/images/leonardo.jpg',
		'donny': 'vanishingNinjas/images/donatello.jpg',
		'raf': 'vanishingNinjas/images/raphael.jpg',
		'mike': 'vanishingNinjas/images/michelangelo.jpg',
		'april': 'vanishingNinjas/images/april.jpg'
	}
	if color == '':
		context['all'] = True
	elif color == 'blue':
		context['color'] = 'blue'
	elif color == 'purple':
		context['color'] = 'purple'
	elif color == 'red':
		context['color'] = 'red'
	elif color == 'orange':
		context['color'] = 'orange'
	return render(request, 'vanishingNinjas/ninjas.html', context)