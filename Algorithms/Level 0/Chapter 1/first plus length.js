var arrNum = [5, 8, 9, 1, 11];
var arrStr = ['luke', 'yoda', 'mace', 'obi-wan', 'anakin'];
var arrBool = [true, true, false, true, false];
var sum = 0;

function firstPlusLast(arg1) {
	sum = arg1[0] + arg1.length;
	return sum;
}
firstPlusLast(arrNum);
firstPlusLast(arrStr);
firstPlusLast(arrBool);
console.log(firstPlusLast(arrNum));
console.log(firstPlusLast(arrStr));
console.log(firstPlusLast(arrBool)); // a true == 1, so true + arrBool.length = 6