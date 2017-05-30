# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import SecretDB, LikeDB, UserDB

# register method --> logReg controller
# login method --> logReg controller

def home(request):
	context = {
		'allSecrets': SecretDB.objects.all()
	}
	return render(request, 'secrets/index.html', context)

def newSecret(request):
	if request.method == 'POST':
		# currentUser is the author of a secret post
		currentUser = UserDB.objects.get(id=request.session['user']['id'])
	# ****** CHECK DATA SECTION *******
		print '*'*50
		print 'LOOKING', currentUser
		print '*'*50
		# ****** END CHECK *******
		response = SecretDB.objects.postSecret(currentUser, request.POST)
		if not response[0]:
			for message in response[1]:
				return redirect('secrets:home')
		else:
			if response[0]:
				return redirect('secrets:home')
	return redirect('secrets:home')

def popular(request):
	pass
	return render(request, 'secrets/mostLiked.html')

def logout(request):
	pass
	return redirect('secrets:index')

def delete(request, id):
	pass
	return redirect('secrets:home')

def like(request, id):
	pass
	if home:
		return redirect('secrets:home')
	elif popular:
		return redirect('secrets:popular')
		