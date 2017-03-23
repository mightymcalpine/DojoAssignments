var testArr = [56, 'luke', Infinity, 1984, 'lightsaber'];
var newArr = [];

function onlyNum(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (typeof arr[x] === "number") {
			newArr.push(arr[x]);
		}
	}
	return newArr;
}
console.log(onlyNum(testArr));

// function removeNum(arr) {
// 	for (var x = 0; x < arr.length; x++) {
// 		if (typeof arr[x] === 'number') {
// 			arr.splice(x, 1);
// 		}	
// 	}
// 	console.log(testArr2);
// }
// console.log(removeNum(testArr2));