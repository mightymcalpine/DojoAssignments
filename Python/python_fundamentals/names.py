#           ** Part I **
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def names():
	for val in students:
		print val['first_name'], val["last_name"]
names()

# 	     ** Part II **

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentsInstructors():
    for item in users:
        print item
        counter = 0        
        for person in users[item]:
            length = len(person['first_name']) + len(person['last_name'])
            counter += 1
            print counter, '-', person['first_name'], person['last_name'], '-', length
studentsInstructors()
	