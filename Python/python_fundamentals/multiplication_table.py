topRow = 'x  1  2  3  4  5  6  7  8  9  10  11  12'
firstColumn = 0
print topRow
for x in range(1, 13):
	firstColumn += 1
	print firstColumn	

# can't quite figure out the formating

def multTable():
	for row in range(1, 13):			
		for col in range(1, 13):			
			print row * col,
		print
multTable()
