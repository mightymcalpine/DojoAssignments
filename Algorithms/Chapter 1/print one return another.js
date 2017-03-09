var testArr = [72, 9, 21, 76, 116, 512, 723, 11, 356, 2, 39, 91, 897];
var firstOddNum = 0;

function firstOdd(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] % 2 !== 0) {
			firstOddNum = arr[x];
			break;
		}
	}
	console.log(arr[arr.length - 2]);
	return firstOddNum;
}
firstOdd(testArr);
