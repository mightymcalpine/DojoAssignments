tblRow = 'x 1 2 3 4 5 6 7 8 9 10 11 12'
print tblRow

var2 = 0

def operand2(runnerNum):	
	firstColumn = 0
	for numDown in range(1, 13):
		firstColumn += 1	
		var = numDown * runnerNum		print firstColumn, var
operand2(var2)

for numAcross in range(1, 13):
	var2 = numAcross
	operand2(var2)	
	

