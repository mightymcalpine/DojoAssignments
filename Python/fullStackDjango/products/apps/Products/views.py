# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import Product

# View Methods
def index(request):
	pro1 = Product.objects.create(name = 'Breville Power Spin Blender', description = 'the most powerful spinniest blender of all time', weight = '25', price = '$550.95', cost = '$495', category = 'kitchen appliances')
	pro2 = Product.objects.create(name = 'Nike Air Maxx', description = 'running shoes with soles filled with air', weight = '1', price = '$160', cost = '$140', category = 'running shoes')
	pro3 = Product.objects.create(name = 'Felt F55', description = 'lightweight fast road bike', weight = '20', price = '$1999.99', cost = '$1299', category = 'road bikes')
	
	allProducts = Product.objects.all()

	for product in allProducts:
		print 'ID: ' + str(product.id)+'\n' + 'Name: ' + str(product.name)+'\n' + 'Description: ' + str(product.description)+'\n' + 'Weight: ' + str(product.weight)+'\n' + 'Price: ' + str(product.price)+'\n' + 'Cost: ' + str(product.cost)+'\n' + 'Category: ' + str(product.category)+'\n'
	return render(request, 'Products/index.html')