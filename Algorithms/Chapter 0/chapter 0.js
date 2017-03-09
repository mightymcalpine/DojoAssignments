var myNum = 35;
var myName = 'Lars';
console.log(myName, myNum)

var temp = myNum;
var myNum = myName;
var myName = temp;
console.log(myName, myNum)

var list = [];
for(var x = -52; x < 1067; x++) {
	// list.push(x);
} 
console.log(list)

function beCheerful(argument) {
	for(var x = 1; x < 99; x++) {
		console.log('Good Morning!');	
	}
}
// beCheerful()

for(var x = -300; x < 1; x++) {
	if(x % 3 == 0) {
		if(x == -6) {
			continue;
		}
		if(x == -3) {
			continue;
		}
	else
		// console.log(x);
		break;
	}
}

var number = 2000;
while(number < 5281) {
	console.log(number);
	number++
	break
}

function birthday(day, month) {
	if(day == 25 && month == 4) {
		console.log('Birthday!');
	}
	else if(day == 4 && month == 25) {
		console.log('Birthday!');
	}
	else
		console.log('Just another day');
}
// birthday(25, 4)
// birthday(4, 25)
birthday(3, 36)

// function leapYear() {
	for(var y = 1800; y <= 2400; y += 4){ 
		if(y % 4 == 0) {
			if(y % 400 != 0) {
				if(y % 100 != 0) {
					console.log(y, 'is a Leap Year');
				}
				else {
					console.log(y, 'is not Leap Year');
				}
			}
			else {
				console.log(y, 'is a Leap Year');
			}
		}
		else { 
			console.log(y, 'is not Leap Year');
		}
	}
// }	
// leapYear(2016)
// leapYear(2000)
// leapYear(2400)

