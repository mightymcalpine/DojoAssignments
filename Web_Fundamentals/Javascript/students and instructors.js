// 			***** PART I *****
// var students = [ 
//      {first_name:  'Michael', last_name : 'Jordan'},
//      {first_name : 'John', last_name : 'Rosales'},
//      {first_name : 'Mark', last_name : 'Guillen'},
//      {first_name : 'KB', last_name : 'Tonel'}
// ]
// function firstNameLastName(students) {
// 	for (var x = 0; x < students.length; x++) {
// 		console.log(students[x].first_name, students[x].last_name);
// 	}
// }
// firstNameLastName(students);

// 			***** PART II *****
var users = {
 Students: [ 
     {first_name: 'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 Instructors: [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

 function studentNameInstructorName(users) {
 	for (var userGroup in users) {
 		console.log(userGroup);
	 	var counter = 0;
	 	var userList = users[userGroup];
	 	for (var x = 0; x < userList.length; x++) {
	 		counter++;
	 		var user = userList[x];
	 		var nameLength = user.first_name.length + user.last_name.length;
	 		console.log(counter + ' - ' + user.first_name, user.last_name + ' - ' + nameLength);
		}
 	}
 }
 studentNameInstructorName(users);
 
 
 
 