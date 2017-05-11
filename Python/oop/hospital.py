import random

class Patient(object):
	# init method run for every instance of Patient class
	def __init__(self, id, name, ailment):
		self.id = id
		self.name = name
		self.ailment = ailment
		self.bedNumber = 0
	
	def patientInfo(self):
		print 'Patient Card:'+'\n' + 'Name: ' + str(self.name)+'\n' + 'ID: ' + str(self.id)+'\n' + 'Reason for visit: ' + str(self.ailment)

patient0 = Patient(0, 'Dexter Cogsworth', "zombie-like symptoms")
# print patient0.patientInfo()
patient1 = Patient(6, 'Julius Winfield', "severed toe")
# print patient1.patientInfo()
patient2 = Patient(12, 'Shay Wheeler', "concussed")
# print patient2.patientInfo()
patient3 = Patient(18, 'Barty McFly', "complications from time travel")
patient4 = Patient(24, 'Chet Crowder', "lazy eye")

class Hospital(object):
	# init method run for every instance of Hospital class
	def __init__(self, name):
		self.patients = [] 
		self.name = name
		self.bedNumber = 0
		self.patientQueue = 0
		self.maxCapacity = 4
	
	def admit(self, *patients):
		for person in patients:
			if len(self.patients) >= self.maxCapacity:
				print 'We are sorry ' + str(person.name) + ' but the hospital is full'
			else:
				self.bedNumber += 1
				person.bedNumber = self.bedNumber
				self.patients.append(person)
				print 'Welcome to Breckenridge ' + str(person.name)
		self.patientQueue = len(self.patients)
		return self
	
	def discharge(self, id):
		for person in self.patients:
			if person.id == id:
				self.patients.remove(person)
				print str(person.name) + ' has been discharged'
				person.bedNumber = 0			
		self.patientQueue = len(self.patients)
		return self
	
	def show(self):
		print 'Regional Hospital:'+'\n' 'Name: ' + str(self.name)+'\n' + 'Number of Patients: ' + str(self.patientQueue)+'\n' + 'Max Capacity: ' + str(self.maxCapacity)+'\n' + 'Current Patient Queue:'
		for person in self.patients:
			print 'patient name: ' + str(person.name)+'\n' + 'bed number: ' + str(person.bedNumber)

hospital1 = Hospital('Breckenridge')
hospital1.admit(patient0, patient1, patient2, patient3, patient4).show()		