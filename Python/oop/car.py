class car(object):	
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0
		self.salesTax().display()
	
	def display(self):
		print 'Price:', self.price
		print 'Top Speed:', self.speed
		print 'Fuel Level:', self.fuel
		print 'Mileage:', self.mileage
		print 'Sales Tax:', self.tax
		print '' #spacer
		return self
	
	def salesTax(self):
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		return self
	
porsche = car(150000, 200, 'full', '21 mpg')
ferrari = car(249000, 225, 'full', '15 mpg')
bugatti = car(2700000, 262, 'half-full', '15 mpg')
lamborghini = car(325000, 205, 'draining fast', '16 mpg')
mclaren = car(1500000, 249, 'full', '12 mpg')
destroyed_aston_martin = car(1000, 0, 'empty', '0 mpg')		