function arrayCount(x) {
	var sum = 0;
	for(var i = 0; i < x.length; i++) {
		sum = sum + x[i];
	}
	console.log(sum);
}
arrayCount([1, 9, 8, 4, 8]);
