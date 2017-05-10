# parent class to create animal object
class animal(object):
	# init method run for every instance of animal class
	def __init__(self, name, health=100):
		self.name = name
		self.health = health
	
	# chainable method adds to health attribute
	def walk(self):
		self.health -= 1
		return self
	
	# chainable method adds to health attribute
	def run(self):
		self.health -= 5
		return self
	
	# chainable method displays object name and health attributes
	def showHealth(self):
		print 'Name: ' + str(self.name)+'\n' + 'Health: ' + str(self.health)+'\n'
		
# Dog child class inherits from animal class
class dog(animal):
	# init method run for every instance of animal class
	def __init__(self, name, health=150):
		super(dog, self).__init__(name, health)
		# self.health = health
	def pet(self):
		self.health += 5
		return self
	

# Dog child class inherits from animal class
class dragon(animal):
	# init method run for every instance of animal class
	def __init__(self, name, health=170):
		super(dragon, self).__init__(name, health)
		self.health = health
	def fly(self):
		self.health -= 10
		return self
	def showDragonHealth(self):
		print 'Smaug is awfully deadly indeed'
		self.showHealth()


# create instance of animal class
firstAnimal = animal('MegaWolf')
print firstAnimal.walk().walk().walk().run().run().showHealth()

# create instance of dog class
firstDog = dog('ThunderDog')
print firstDog.walk().walk().walk().run().run().pet().showHealth()

# create instance of dog class
firstDragon = dragon('Smaug')
print firstDragon.walk().walk().walk().run().run().fly().fly().showDragonHealth()

# Run the checks below to verify that each child class is ONLY inheriting from the animal parent class

# firstSnake = animal('anaconda')
# print firstSnake.fly().pet().showHealth()

# print firstDog.fly().showHealth()










		