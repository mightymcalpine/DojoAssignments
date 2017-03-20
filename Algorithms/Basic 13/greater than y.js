var arr = [3, 6, 9, 12, 15, 91, 18, 21];
var y = 70;
for (var x = 0; x < arr.length; x++) {
	var sum = 0;
	if (arr[x] > y) {
		sum++;
		console.log(arr[x]);
	}
}