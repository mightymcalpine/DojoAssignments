//  Given an array arr and a number num, multiply all values in arr by num,
// 	and return the changed array arr.

var arr = [6, 12, 36, 7];
var num = 3;

function scaleArray(arg1) {
	for (var x = 0; x < arr.length; x++) {
		arr[x] *= num;	
	}
	return arg1;
}
console.log(scaleArray(arr));