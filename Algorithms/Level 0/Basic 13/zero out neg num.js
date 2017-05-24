var testArr = [3, -6, 9, -12, 15, -91, 18, -21];

function zeroNegNum(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] < 0) {
			arr[x] = 0;
		}	
	}
	return arr;
}
console.log(zeroNegNum(testArr));