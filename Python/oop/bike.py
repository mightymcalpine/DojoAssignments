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
		return self
		
	def reverse(self):
		print 'Reversing'
		if self.miles >= 5:
			self.miles -= 5
		return self
	
unoBike = bike(100, '15 mph')
dosBike = bike(500, '25 mph')
tresBike = bike(950, '35 mph')
print unoBike.ride().ride().ride().reverse().displayInfo()
print dosBike.ride().ride().reverse().reverse().displayInfo()
print tresBike.reverse().reverse().reverse().displayInfo()