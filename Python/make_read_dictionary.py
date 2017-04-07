mclp = {
	'name': 'Lars',
	'age': 35,
	'origin': 'USA',
	'lang': 'Python'
}

def aboutMe(obj):
	print 'My name is', obj['name']
	print 'My age is', obj['age']
	print 'My country of origin is', obj['origin']
	print 'My favorite language is', obj['lang']
aboutMe(mclp)

