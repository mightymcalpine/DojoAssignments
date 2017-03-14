var testArr1 = [2, 4, 6, 8, 10, 12, 14, 16];
var testArr2 = [12, 12, 12, 12, 12, 12];
var num = 3;

function lastFew(arr) {
	var reduce = arr.length - num;
	for (var x = 0; x < reduce; x++) {
		arr.shift();
	}
	return arr;
}
console.log(lastFew(testArr2));