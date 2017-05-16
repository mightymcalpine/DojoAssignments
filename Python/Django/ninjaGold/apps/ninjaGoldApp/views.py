# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint

from django.contrib import messages
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render


# Create your views here.
def index(request):
	messages.add_message(request, messages.INFO, 'Dub Train')
	return render(request, 'ninjaGoldApp/index.html')

# def processGold(request):
# 	if request.method == 'POST':
		