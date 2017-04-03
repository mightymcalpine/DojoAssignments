# 			** MULTIPLES **
# Part I
for x in range(1, 1000, 2):
	print x	

# Part II
for x in range(5, 1000000, 5):
	print x	

#			** SUM LIST **
a = [1, 2, 5, 10, 255, 3]
sum = 0
for x in a:
	sum += x
print sum

#			** AVERAGE LIST **
a = [1, 2, 5, 10, 255, 3]
sum = 0
for x in a:
	sum += x
avg = sum / len(a)
print avg
