# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import render
from time import strftime

# Create your views here.
def index(request):
	print 'METHOD:', request.method
	timeDate = {
		'rightNow': strftime('%I:%M %p %m-%d-%Y')
	}
	return render(request, 'index.html', timeDate)