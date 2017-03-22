function printRange(start, end, skip) {
	skip = skip > 0 ? skip : 1;
	for (var x = start; x < end; x += skip) {
		console.log(x);
	}
}
printRange(4, 16, 4);