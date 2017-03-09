var total = 0;
for (var x = 512; x <= 4096; x++) {
	if (x % 5 == 0) {
		total++;
		console.log(x);
	}
}
console.log('There are ' + total + ' multiples of 5 between 512 and 4096');
// view of console output is limited