# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint

from django.contrib import messages
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from time import strftime

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'bank' not in request.session:
		request.session['bank'] = 0
	if 'gameActivity' not in request.session:
		request.session['gameActivity'] = []
	return render(request, 'ninjaGoldApp/index.html')

def processGold(request):
	if request.method == 'POST':
		request.session['bank'] = request.session['gold']
		if request.POST['building'] == 'farm':
			request.session['gold'] += randint(10 ,20)
		# if gold is > 100, flash a message to try casino
		elif request.POST['building'] == 'cave':
			request.session['gold'] += randint(5, 10)
		elif request.POST['building'] == 'house':
			request.session['gold'] += randint(2, 5)
		elif request.POST['building'] == 'casino' and request.session['bank'] == 0:
			messages.add_message(request, messages.INFO, 'Casino has a 5 gold cover charge')
		elif request.POST['building'] == 'casino' and request.session['gold'] < -100:
			messages.add_message(request, messages.INFO, 'You are now 100 golds in debt, time for you to get some more gold before we let you play here again')
		elif request.POST['building'] == 'casino':
			winLossRatio = randint(1, 100)
			if winLossRatio <= 40:
				request.session['gold'] += randint(0, 50)
			else:
				request.session['gold'] -= randint(0, 50)
		
		request.session['building'] = request.POST['building']
		request.session['goldThisRound'] = request.session['gold'] - request.session['bank']
		request.session['time'] = strftime("%I:%M:%S")
		
		if request.session['goldThisRound'] > 0:
			request.session['gameActivity'].append('<p id="win-msg">' + 'You won ' + str(request.session['goldThisRound']) + ' gold from the ' + request.session['building'] + ' ' + request.session['time'] + '</p>')
		elif request.session['goldThisRound'] < 0 and request.session['building'] == 'casino':
			request.session['gameActivity'].append('<p class="fail-msg">' + 'Bummer you lost ' + str(request.session['goldThisRound']) + ' gold from the ' + request.session['building'] + ' ' + request.session['time'] + '</p>')
		return redirect('/')
	else:
		return redirect('/')

def reset(request):
	if request.method == 'GET':
		request.session.clear()
		return redirect('/')