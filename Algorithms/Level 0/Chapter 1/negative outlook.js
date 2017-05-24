var testArr = [56, 1984, 12, 6,];
var newArr = [];

function negativeOutlook(arr) {
	for (var x = 0; x < arr.length; x++) {
		arr[x] = -arr[x];
		newArr.push(arr[x]);
	}
	return newArr;
}
negativeOutlook(testArr);