var testArr1 = [1, 2, 3, 4, 5, 6];
var testArr2 = ['pizza', 42, 'Ada', 2, true, 'golf'];

// 	** WHILE loop version **
function swapToCenter(arr) {
	var left = 0;
	var right = arr.length - 1;
	while	(left < right) {
		var temp	= arr[left];
		arr[left] = arr[right];
		arr[right] = temp;
		left += 2;
		right -= 2;
	}
	return arr;
}
console.log(swapToCenter(testArr2));


// 	** FOR loop version **
function swapCenter(arr) {
	var midPoint = arr.length/2;
	for (var x = 0; x < midPoint; x += 2) {
		var right = arr.length -1 -x;
		var temp = arr[x];
		arr[x] = arr[right];
		arr[right] = temp;
	}
	return arr;
}
console.log(swapCenter(testArr1));