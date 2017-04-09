def fooBar():
	for num in range(100, 100001):
	  sqrt = num ** (0.5)
	  sqrt2 = int(sqrt * 100)
	  for number in range(2,11):
			print number
			if sqrt2 % 100 == 0: # perfect square
				print sqrt2      	
				print 'Bar'
				break
			# elif num == 0 or num == 1: # prime number
			# 	print num	      	
			# 	print 'Foo'
			# 	break
			elif (num % number == 0) and (num != number):
				print num      		
				print 'FooBar'
				break
			else:
				print num
				print 'Foo'				 	          	
				break

fooBar()