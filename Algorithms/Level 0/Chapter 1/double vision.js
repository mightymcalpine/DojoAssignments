var testArr = [3, 6, 28, 42];
var doubledArr = [];

function doubleEachOne(arr) {
	for (var x = 0; x < arr.length; x++) {
		arr[x] *= 2;
		doubledArr.push(arr[x]);
	}
	return doubledArr;
}
doubleEachOne(testArr);