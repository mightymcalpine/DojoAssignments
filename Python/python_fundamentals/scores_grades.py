import random

def scoresGrades():
	for x in range(10):
		random_num = random.randint(60, 100)
		# print random_num
		if (random_num >= 90):
			print 'Score: {}; Your grade is A'.format(random_num)
		elif (random_num >= 80):
			print 'Score: {}; Your grade is B'.format(random_num)
		elif (random_num >= 70):
			print 'Score: {}; Your grade is C'.format(random_num)
		elif (random_num >= 60):
			print 'Score: {}; Your grade is D'.format(random_num)
	return 'End of the Program. Bye!'
rst = scoresGrades()
print rst

