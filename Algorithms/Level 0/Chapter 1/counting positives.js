var testArr = [72, -9, -21, -76, 116, -512, -723, 11, 356, -2, -39, -91, -897];
var positiveNums = 0;

function countPositives(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] > 0) {
			positiveNums++
		}
	}
	arr[arr.length - 1] = positiveNums;
	return testArr;
}
countPositives(testArr);