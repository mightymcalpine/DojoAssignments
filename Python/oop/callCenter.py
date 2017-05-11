class Call(object):
	# init method run for every instance of Call class
	def __init__(self, id, name, pNumber, timeStamp, reason):
		self.id = id
		self.name = name
		self.pNumber = pNumber
		self.timeStamp = timeStamp
		self.reason = reason
	
	def showCall(self):
		print 'Call ID: ' + str(self.id)+'\n' + 'Caller Name: ' + str(self.name)+'\n' + 'Phone Number: ' + str(self.pNumber)+'\n' + 'Time of Call: ' + str(self.timeStamp)+'\n' + 'Reason for Call: ' + str(self.reason)+'\n'

# instances of the Call class
caller1 = Call(100, 'Barty McFly', '555-555-5555', '2:22 pm', 'troubled about many things')
caller2 = Call(101, 'Stoney McFranklin', '666-666-6666', '11.56 am', 'hearing voices, concerned')
caller3 = Call(102, 'Sid Victor', '777-777-7777', '9:36 am', 'thinks he saw a ghost, freaked out')
caller1.showCall()
caller2.showCall()
caller3.showCall()

class CallCenter(object):
	# init method run for every instance of CallCenter class
	def __init__(self):
		self.calls = []
		self.queueSize = 0
	
	# pass in one or more caller objects, add new object to calls list 
	def addCall(self, *calls):
		for call in calls:
			self.calls.append(call)
		self.queueSize = len(self.calls) 
		return self
	
	# remove the first caller/object from the calls list
	def removeCall(self):		
		del self.calls[0]
		return self
	
	# pass in phone number of caller you want removed from list of calls
	def removeByNumber(self, pNumber):
		for call in self.calls:
			if call.pNumber == pNumber:				
				self.calls.remove(call)
		print str(call.name) + ' has been removed from the records'+'\n'	
		return self
	
	# display method, loops through calls list 
	def callInfo(self):
		print 'Call Center Call Log:'
		for call in self.calls:
			print 'Caller Name: ' + str(call.name)+'\n' + 'Phone Number: ' + str(call.pNumber)+'\n'
		print 'Number of Calls in Queue: ' + str(self.queueSize)

# instance of the CallCenter class
ccLog = CallCenter()
print ccLog.addCall(caller1, caller2, caller3).removeByNumber('666-666-6666').callInfo()