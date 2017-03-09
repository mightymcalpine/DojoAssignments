testArr1 = [3, 10, 2, 19, 21, 56, 7, 1984]
testArr2 = [9]; // based on the instruction for this algorithm, testArr2 will return an empty array

var newArr = [];
var total = 0;
function greatThanSecond(arg1) {
	for (var x = 0; x < arg1.length; x++) {
		if (arg1[x] > arg1[1]) {
			newArr.push(arg1[x]);
			total++;
		}
	}
	return newArr;
}
greatThanSecond(testArr1);
console.log(total); 