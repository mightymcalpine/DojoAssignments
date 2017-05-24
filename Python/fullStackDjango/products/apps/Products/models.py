# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length = 64)
	description = models.CharField(max_length = 255)
	weight = models.IntegerField()
	price = models.CharField(max_length = 16)
	cost = models.CharField(max_length = 16)
	category = models.CharField(max_length = 64)