def checkerBoard():
	star = '*'
	space = ' '
	for position in range(8):
		if position % 2 == 0:
			print star, space, star, space, star, space, star, space
		else:
			print space, star, space, star, space, star, space, star
checkerBoard()