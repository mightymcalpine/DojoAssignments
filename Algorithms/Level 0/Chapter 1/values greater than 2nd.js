// directions stated greater than second value, not second index

var arr = [1,3,5,7,9,13]; // second value is 3, there are 4 elements greater than 3
var sum = 0;

function greaterThanSecond(arg1) {
	for (var x = 0; x < arg1.length; x++) {
		if (arg1[x] > arg1[1]) {
		console.log(arg1[x]); // print elements great than 3
		sum++; // add 1 to sum for each element greater than 3	
		}
	}
	return sum;
}
console.log(greaterThanSecond(arr));