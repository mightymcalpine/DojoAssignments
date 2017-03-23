// 			***** PART I *****
var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]
function firstNameLastName(students) {
	for (var x = 0; x < students.length; x++) {
		// console.log(students[x].first_name, students[x].last_name);
	}
}
firstNameLastName(students);

// 			***** PART II *****
var users = {
 Students: [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 Instructors: [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

 function studentNameInstructorName(students, instructors) {
 	console.log('Students');
 	var counter = 0;
 	for (var x = 0; x < students.length; x++) {
 		counter++;
 		var nameLength = users.Students[x].first_name.length + users.Students[x].last_name.length;
 		console.log(counter + ' - ' + users.Students[x].first_name, users.Students[x].last_name + ' - ' + nameLength);
 	}
 	console.log('Instructors');
 	counter = 0;
 	for (var x = 0; x < instructors.length; x++) {
 		counter++;
 		nameLength = users.Instructors[x].first_name.length + users.Instructors[x].last_name.length;
 		console.log(counter + ' - ' + users.Instructors[x].first_name, users.Instructors[x].last_name + ' - ' + nameLength)
 	}
 }
 studentNameInstructorName(users.Students, users.Instructors);