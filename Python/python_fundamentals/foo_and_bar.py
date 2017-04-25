def fooBar():
	for num in range(100, 100001):
	  sqrt = num ** (0.5)
	  sqrt2 = int(sqrt * 100)
	  for number in range(2,11):
			if sqrt2 % 100 == 0: # perfect square				      	
				print 'Bar', sqrt2, 'is a perfect square'
				break
			elif num == 0 or num == 1: # prime number					      	
				print 'Foo', num, 'is a prime number'
				break
			elif (num % number == 0) and (num != number):				      		
				print 'FooBar', num, 'is neither of prime nor perfect'
				break
			else:			
				print 'Foo', num, 'is a prime number'			 	          	
				break
fooBar()