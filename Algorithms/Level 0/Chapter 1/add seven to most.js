var testArr = [49, 77, 5, 1, 49];
var newArr = [];

function addSeven(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (x == 0) {
			continue
		}
		else {
			arr[x] += 7;
			newArr.push(arr[x]);
		}
	}
	return newArr;
}
addSeven(testArr);