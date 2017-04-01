function printRange(start, end, skip) {
	skip = skip === undefined ? 1 : skip;
	for (var x = start; x < end; x += skip) {
		console.log(x);		
	}
	if (start > end) {
		for (var x = start; x > end; x -= skip) {
			console.log(x);
		}
	}
	if (end === undefined) {
		for (var x = 0; x < start; x++) {
			console.log(x);
		}
	}
}
printRange(4);