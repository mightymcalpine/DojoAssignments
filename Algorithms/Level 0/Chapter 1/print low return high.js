var testArr = [71, 9, 21, 76, 116, 512, 11, 356, 2, 39, 91, 897]
var highestNum = 0;
var lowestNum = testArr[0];

function returnHigh(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] > highestNum) {
			highestNum = arr[x];
		}
		if (arr[x] < lowestNum) {
			lowestNum = arr[x];
		}
	}
	console.log(lowestNum);
	return highestNum;
}
returnHigh(testArr);
