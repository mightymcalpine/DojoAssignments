# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
	title = models.CharField(max_length = 96)
	author = models.CharField(max_length = 96)
	published_date = models.CharField(max_length = 24)
	category = models.CharField(max_length = 96)
	in_print = models.BooleanField(True)