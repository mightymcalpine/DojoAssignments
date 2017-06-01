# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import SecretDB, LikeDB, UserDB

# register method --> logReg controller
# login method --> logReg controller 

def home(request):
	context = {
		# could refactor this query to a method in models
		'allSecrets': SecretDB.objects.all().order_by('-createdAt')[:5],
		'allLikes': LikeDB.objects.all()
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
				# ****** CHECK DATA SECTION *******
				print '#'*50
				print response[1].secret
				print '#'*50
				# ****** END CHECK *******
				return redirect('secrets:home')
	return redirect('secrets:home')

def popular(request):
	context = {
		# sort this by DESC, most liked
		'allSecrets': SecretDB.objects.all()
	}
	return render(request, 'secrets/mostLiked.html', context)

def logout(request):
	pass
	return redirect('secrets:index')

def delete(request, id):
	SecretDB.objects.get(id=id).delete()
	return redirect('secrets:home')

def like(request, id):
	secretID = SecretDB.objects.get(id=id)
	authorID = UserDB.objects.get(id=request.session['user']['id'])
	# pass secretID and authorID to the likeSecret chief
	response = LikeDB.objects.likeSecret(secretID, authorID)
	# ****** CHECK DATA SECTION *******
	print '#'*50
	print 'WHAT THIS newLike', response.secret.author.id
	print '#'*50
	# ****** END CHECK *******
	if request.session['user']['id'] == response.secret.author.id:
		print True
	
	
	
	
	return redirect('secrets:home')










		