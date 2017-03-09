var testArr = ['luke', 'vader', 'yoda', 'sidious'];
var tempArr = [];

function previousLength(arr) {
	tempArr.push(arr[x]);
	for (var x = 0; x < arr.length; x++) {
		if (x == 0) {
			arr[x] = arr[arr.length - 1].length;
		}
		if (x !== 0) {
			arr[x] = tempArr[x - 1];
		}	
	}	
	return arr;
}
console.log(previousLength(testArr));