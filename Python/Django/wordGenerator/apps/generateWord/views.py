# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib2, random

from django.shortcuts import redirect
from django.shortcuts import render

wordSource = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
response = urllib2.urlopen(wordSource)
renderText = response.read()
rand_sel_word = renderText.splitlines()

def index(request):
	randomWord = random.choice(rand_sel_word)
	if 'attempt' in request.session:
		request.session['attempt'] += 1
	else:
		request.session['attempt'] = 1
	words = {
		'word': randomWord,
		'attempt': request.session['attempt']
	}
	return render(request, 'index.html', words)

def reset(request):
	request.session.clear()
	return redirect('/')
