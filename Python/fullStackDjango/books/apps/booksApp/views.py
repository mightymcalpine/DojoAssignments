# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import Books

def index(request):
	book1 = Books.objects.create(title = 'Star Wars A New Hope', author = 'John Guy', published_date = 'January 21, 1977', category = 'science fiction', in_print = True)
	book2 = Books.objects.create(title = 'How to Win at Life', author = 'Bart Winnington', published_date = 'May 6, 1987', category = 'self help', in_print = False)
	book3 = Books.objects.create(title = 'Lost in Space', author = 'Bill Guymore', published_date = 'October 22, 1923', category = 'fiction', in_print = False)
	book4 = Books.objects.create(title = 'My Life', author = 'Bill Clinton', published_date = 'June 8, 1999', category = 'memoir', in_print = True)
	book5 = Books.objects.create(title = '1984', author = 'George Orwell', published_date = 'July 12, 1946', category = 'dystopian', in_print = True)
	allBooks = Books.objects.all()
	for book in allBooks:
		print 'ID:', book.id, '\nTitle:', book.title, '\nAuthor:', book.author, '\nDate Published:', book.published_date, '\nCategory:', book.category, '\nCirculation:', book.in_print
	return render(request, 'booksApp/index.html')