var testArr = ['luke', 'R2', 'hsolo', 'sidious'];

function prevLength(arr) {
	var previous = arr[arr.length - 1].length
	var current;
	for (var x = 0; x < arr.length; x++) {
		current = arr[x].length;
		arr[x] = previous;
		previous = current	
	}
	return arr;
}
console.log(prevLength(testArr));