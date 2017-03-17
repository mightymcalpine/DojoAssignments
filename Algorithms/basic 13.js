for (var x = 1; x < 256; x++) {
		console.log(x);
}

for (var x = 1; x <= 255; x += 2) {
	console.log(x);
}

var sum = 0;
for (var x = 0; x <= 255; x++) {
	console.log(x);
	sum += x;
	console.log(sum);
}

testArr = [1, 2, 3, 4, 5]
for (var x = 0; x < testArr.length; x++) {
	console.log(arr[x]);
}

testArr = [1, 2, 3, 4, 5, 6, 41, 7]
var max = 0;
for (var x = 0; x < arr.length; x++) {
	if (arr[x] > max) {
		max = arr[x];
	}
}

testArr = [1, 2, 3, 4, 5, 6, 41, 7]
var sum = 0;
for (var x = 0; x < arr.length; x++) {
	sum += arr[x];		
}
console.log(sum / arr.length);

var testArr = [];
for (var x = 1; x <= 255; x += 2) {
		testArr.push(arr[x]);
}
console.log(testArr);

testArr = [1, 2, 3, 4, 5]
for (var x = 0; x < testArr.length; x++) {
	testArr[x] *= testArr[x];
}

var testArr = [1, 4, 8, 11, 3, 19]
var y = 7;
var sum = 0
for (var x = 0; x < testArr.length; x++) {
	if (testArr[x] > y) {
		sum++;
		console.log(testArr[x]);
	}
}

var testArr = [1, 4, -8, -11, 3, -19];
for (var x = 0; x < arr.length; x++) {
	if (testArr[x] < 0) {
		testArr[x] = 0;
	}
}
console.log(testArr);

var testArr = [1, 4, 8, 11, 86, 22, 3, 19, 47];
var max = 0;
var min = testArr[0];
var sum = 0;
var avg = 0;
function maxMinAvg(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] > max) {
			max = arr[x];
		}
		if (arr[x] < min) {
			min = arr[x];
		}
		sum++;
	}
	avg = sum / arr.length;
	return max, min, avg;
}
maxMinAvg(testArr);






