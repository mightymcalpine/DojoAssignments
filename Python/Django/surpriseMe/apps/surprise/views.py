# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.contrib import messages
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

values = ['Luke skywalker is a jedi master', 'darth vader is a sith lord', 'han solo is a smuggler', 'leia Organa is a princess', 'C3P0 is a robot', 'someday pigs will take flight']

# Create your views here.
def index(request):
	return render(request, 'surprise/index.html')
	
def results(request):
	if request.method == 'POST':
		number = int(request.POST['number'])				
		random.shuffle(values)		
		context = {
			'newList': []
		}
		if number > len(values):
			messages.add_message(request, messages.INFO, "ooh too bad, looks like we don't have that many things, try a smaller number")
			return redirect('/')
		else:
			for num in range(0, number):				
				context['newList'].append(values[num])
		return render(request, 'surprise/results.html', context)