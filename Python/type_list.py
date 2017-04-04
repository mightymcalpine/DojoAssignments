ls1 = range(3)
ls2 = ['luke', 'han', 'leia', 'c3po']
ls3 = ['vader', 56, 1984, 'sidious']

def typeList(data):
	newStr = ''
	sum = 0
	for x in data:
		if isinstance(x, int):
			sum += x
		if isinstance(x, str):
			newStr += x + ' '		
	if newStr == '':		
		print "The array you entered is of integer type"
		print "Sum:", sum	
	elif sum == 0:	
		print "The array you entered is of string type"
		print "String: " + newStr		
	elif sum != 0 and newStr != '':
		print "The array you entered is of mixed type"
		print "String: " + newStr
		print "Sum:", sum			
typeList(ls3)