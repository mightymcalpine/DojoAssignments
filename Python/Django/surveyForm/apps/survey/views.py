# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'survey/index.html')

def results(request):
	return render(request, 'survey/results.html')

def surveyData(request):
	if request.method == 'POST':
		request.session['user'] = {
			'name': request.POST['name'],
			'location': request.POST['location'],
			'language': request.POST['language'],
			'comments': request.POST['comments'],
		}
		print 'HERE', request.session['user']
		return redirect('/results')
	else:
		return redirect('/')
		