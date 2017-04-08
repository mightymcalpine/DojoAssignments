def primesPerfSq():
	# for num in range(100, 100000):
	for num in range(2, 11):
		for prime in range(2, num):
			if num % prime == 0:
				return False
			else:
				return True
primesPerfSq()