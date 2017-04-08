name = ['luke', 'bane', 'han', 'leia', 'r2d2', 'death star']
trait = ['jedi', 'sith', 'smuggler', 'princess', 'robot', 'battle station']

# This code only works for list of even lengths
def make_dict(arr1, arr2):
	new_dict = {}
	for index in range(len(arr1)):
		print index
		new_dict[arr1[index]] = arr2[index]
	return new_dict
starwars = make_dict(name, trait)
print starwars

	# This code only works for list of even lengths
def make_dict(arr1, arr2):
	zipped = zip(arr1, arr2)
	return dict(zipped)
starwars = make_dict(name, trait)
print starwars

# 	** HACKER CHALLENGE **
def make_dict(arr1, arr2):
	new_dict = {}	
	if len(arr1) > len(arr2):
		length = len(arr1)
		big = arr1
		small = arr2
	else:
		length = len(arr2)
		big = arr2
		small = arr1
	for index in range(length):
		# num of each index in arr
		try:
			new_dict[big[index]] = small[index]
		except IndexError:
			new_dict[big[index]] = None
	return new_dict
starwars = make_dict(name, trait)
print starwars