# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import SecretDB, LikeDB, UserDB

# register method --> logReg controller
# login method --> logReg controller 

def home(request):
	if 'user' in request.session:
		context = {
			# could refactor this queries to a method in models
			'allSecrets': SecretDB.objects.all().order_by('-createdAt')[:5],
			'currentUser': UserDB.objects.get(id=request.session['user']['id'])
		}
		return render(request, 'secrets/index.html', context)
	return redirect('logReg:index')


def newSecret(request):
	if request.method == 'POST':
		# currentUser is the author of a secret post
		currentUser = UserDB.objects.get(id=request.session['user']['id'])
		response = SecretDB.objects.postSecret(currentUser, request.POST)
		if not response[0]:
			for message in response[1]:
				messages.error(request, message[1])
				return redirect('secrets:home')
		else:
			if response[0]:
				return redirect('secrets:home')
	return redirect('secrets:home')

def popular(request):
	context = {
		'allSecrets': SecretDB.objects.annotate(numLikes=Count('secretLike')).order_by('-numLikes'),
		'currentUser': UserDB.objects.get(id=request.session['user']['id'])
	}
	return render(request, 'secrets/mostLiked.html', context)

def delete(request, page, id):
	if page == 'popular':
		SecretDB.objects.get(id=id).delete()
		return redirect('secrets:popular')
	elif page == 'home':
		SecretDB.objects.get(id=id).delete()
		return redirect('secrets:home')

def like(request, page, id):
	secretID = SecretDB.objects.get(id=id)
	authorID = UserDB.objects.get(id=request.session['user']['id'])
	if page == 'popular':
		LikeDB.objects.likeSecret(secretID, authorID)
		return redirect('secrets:popular')
	elif page == 'home':
		LikeDB.objects.likeSecret(secretID, authorID)
		return redirect('secrets:home')