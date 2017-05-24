var arr = [3, 6, 9, 12, 15, 91, 18, 21];
var sum = 0;

for (var x = 0; x < arr.length; x++) {
	sum += arr[x];
}
var avg = sum/arr.length;
console.log(avg);