def testType(data):
	dataType = type(data)
	if dataType == int:
		if data >= 100:
			print "That's a big number!"
		else:
			print "That's a small number"
	if dataType == str:		
		if len(data) >= 50:
			print "Long sentence"
		elif len(data) == 0:
			print "Empty string"
		else:
			print "Short senence"
	if dataType == list:		
		if len(data) >= 10:
			print "Big list!"
		elif len(data) == 0:
			print "Empty list"
		else:
			print "Short list"
testType()	