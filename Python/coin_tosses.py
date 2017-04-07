import random

def coinToss():
	heads = 0
	tails = 0
	print 'Starting the the program...'
	for x in range(5001):	
		coinVal = random.randint(1,2)
		if (coinVal == 1):
			heads += 1
			print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far.".format(x, 'head', heads, tails)		
		else:
			tails += 1
			print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far.".format(x, 'tail', tails, heads)
	return 'End the program, thank you!'
rst = coinToss()
print rst