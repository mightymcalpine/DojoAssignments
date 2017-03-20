var testArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function shiftValues(arr) {
	for (var x = 0; x < arr.length - 1; x++) {
		arr[x] = arr[x + 1];
	}
	arr[arr.length - 1] = 0;
	return arr;
}
console.log(shiftValues(testArr));