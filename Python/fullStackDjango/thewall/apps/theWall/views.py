# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
# from models import 

def index(request):
	return render(request, 'theWall/index.html')
