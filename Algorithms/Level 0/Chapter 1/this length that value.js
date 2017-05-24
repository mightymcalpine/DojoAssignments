var a = 10;
var b = 100;
var arr = [];

function lengthValue(a, b) {
	if (a == b) {
		console.log('Jinx!');
	}
	else {
		while (arr.length < a) {
		arr.push(b);
		}
	}
	return arr;
}
lengthValue(a, b);