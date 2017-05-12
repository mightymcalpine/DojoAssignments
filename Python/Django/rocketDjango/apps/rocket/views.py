# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import render
# the index function is called when the root is visited
def index(request):
	print '#' * 50
	return render(request, "rocket/index.html")
	# response = "Force Power Rising"
	# return HttpResponse(response)
# Create your views here..
