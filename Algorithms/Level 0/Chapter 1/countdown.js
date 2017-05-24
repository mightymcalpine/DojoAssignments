var arr = [];
function countdown(num) {
	for(var x = num; x >= 0; x--) {
		arr.push(x);
	}
	console.log(arr);
	console.log('arr has', arr.length, 'elements')
}
countdown(12);