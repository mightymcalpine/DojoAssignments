var testArr = [6, 'food', 56, 'sith', 'food', 11];
var testArr2 = [6, 9, 11, 12];

function alwaysHungry(arr) {
	var hungry = [];
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] == 'food') {
			console.log('yummy');
		}
		else if (arr[x] !== 'food') {
			hungry.push(arr[x]);
		}
	}
	if (hungry.length > 0) {
		console.log("I'm hungry");
	}
}
alwaysHungry(testArr2);