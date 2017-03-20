var arr = [3, 6, 9, 12, 15, 91, 18, 21];
var max = 0;
for (var x = 0; x < arr.length; x++) {
	if (arr[x] > max) {
		max = arr[x];
	}
}
console.log(max);