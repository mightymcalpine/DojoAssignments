var arr = [5, 11, 19, 5, 22, 55, 87, 83];

function incrementSecond(arg1) {
	for (var x = 1; x < arg1.length; x += 2) {
		arg1[x] += 1;
		console.log(arg1[x]);
	}
	return arr;
}
incrementSecond(arr);