var counter = 0

function bSearch(arr, val) {
	if (!Array.isArray(arr) || arr.length === 0) {
		return false;
	}
	if (counter++ === 100) throw new Error('oops');
	var midPoint = Math.floor(arr.length/2);
	console.log('MIDPOINT:', midPoint, '\n',arr)
	if (arr[midPoint] === val) {
		return true;
	}
	if (arr[midPoint] > val) {
		return bSearch(arr.slice(0, midPoint - 1), val);
	}
	else {
		return bSearch(arr.slice(midPoint + 1), val);
	}
}

testArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];
console.log(bSearch(testArr, 6));