var testArr = [-4, 17, -22, 11, -1, -11, 1386];

function biggieSize(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] > 0) {
			arr[x] = 'big';
		}
	}
	return arr;
}
biggieSize(testArr);