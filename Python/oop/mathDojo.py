class MathDojo(object):
	# init method run for every instance of animal class
	def __init__(self):
		self.result = 0
	
	# chainable method evaluates the multiple inputs based on type
	# adds passed in value to results attribute
	def add(self, *value):
		for val in value:
			if type(val) == int:	
				self.result += val
			elif type(val) == list:
				for item in val:
					self.result += item
			elif type(val) == tuple:
				for val in val:
					self.result += val
		return self

	# chainable method evaluates the multiple inputs based on type
	# subtracts passed in value to results attribute
	def subtract(self, *value):
		for val in value:
			if type(val) == int:	
				self.result -= val
			elif type(val) == list:
				for item in val:
					self.result -= item
			elif type(val) == tuple:
				for val in val:
					self.result -= val
		return self
	
	# display results attribute
	def showResult(self):
	 	print self.result 

# instance of mathdojo class 	
md = MathDojo()
print md.add(1,2,3, (6, 12), [6, 6],).subtract([6, 3], 7, (10, 5)).showResult()
