# FIND and REPLACE
str = "It's thanksgiving day. It's my birthday,too!"
x = str.find('day')
y = len('day')
print 'The position of "day" starts at', x, 'and ends at', x + y
print str.replace('day', 'month')

# print MIN and MAX
x = [56, 1984, 42, 6, -72, 99]
print max(x)
print min(x)

# print FIRST and LAST
x = ['Darth', 56, 1984, 42, 6, -72, 99, 'Bane']
y = [x[0], x.pop()]
print y

# NEW LIST
x = [19,2,54,-2,7,12,98,32,10,-3,6,56]
y = sorted(x)
firstHalf = y[0:len(y)/ 2]
secondHalf = y[len(y)/ 2:len(y)]

newList = []
def joinList():	
	newList.append(firstHalf)
	for x in secondHalf:
		newList.append(x)
joinList()		
print newList