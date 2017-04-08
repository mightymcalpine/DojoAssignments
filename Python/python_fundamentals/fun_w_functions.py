# 		** Odd/Even **
# def oddEven():
# 	for num in range(1, 2001):
# 		if (num % 2 != 0):
# 			print 'Number is {}. This is an odd number.'.format(num)
# 		else:
# 			print 'Number is {}. This is an even number.'.format(num)		
# oddEven()

# 		** Multiply **
def multiply(arr, num):
	for idx in range(len(arr)):
		arr[idx] *= num
	return arr
# a = [2, 4, 10, 16]
# b = multiply(a, 5)
# print b

#		** Hacker Challenge **
def layeredMultiples(arr):
	print arr
	newArray = []
	for x in arr:
		arrVal = []
		for y in range(0, x):
			arrVal.append(1)
		newArray.append(arrVal)	
	return newArray
x = layeredMultiples(multiply([2, 3, 4], 3))
print x