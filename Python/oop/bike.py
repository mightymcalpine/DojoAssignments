class bike(object):
	def __init__(self, price, maxSpeed):
		self.price = price
		self.maxSpeed = maxSpeed
		self.miles = 0
	def displayInfo(self):
		print 'Price is', self.price, 'Top speed is', self.maxSpeed, 'Miles ridden', self.miles
		return self
	def ride(self):
		print 'Riding'
		self.miles += 10
		print self.miles
	def reverse(self):
		print 'Reversing'
		if not self.miles:
			if self.miles >= 5:
				self.miles - 5
	
unoBike = bike(100, '15 mph')
dosBike = bike(500, '25 mph')
tresBike = bike(950, '35 mph')
print 'unoBike:', bike.displayInfo(unoBike).ride()
print 'dosBike:', bike.displayInfo(dosBike)
print 'tresBike:', bike.displayInfo(tresBike)