var testArr = [3, 6, 9, 12, 15, 91, 18, 21];
var max = -Infinity;
var min = Infinity;
var sum = 0;

function maxMinAvg(arr) {
	for (var x = 0; x < arr.length; x++) {
		sum += arr[x];
		min = min < arr[x] ? min : arr[x];
		max = max > arr[x] ? max : arr[x];	
	}
	return [max, min, sum/arr.length];
}
console.log(maxMinAvg(testArr));
