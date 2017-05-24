function threesFives() {
	var sum = 0;
	for (var x = 100; x <= 4000000; x++) {
		if (x % 3 || x % 5) {
			// sum += x;
			if (!(x % 3 && x % 5)) {
			sum += x;
			}
		}
	}
	return sum;
}
console.log(threesFives());

function betterThreesFives(start, end) {
	var sum = 0;
	for (var x = start; x <= end; x++) {
		if (x % 3 || x % 5) {
			if (!(x % 3 && x % 5)) {
			sum += x;
			}
		}
	}
	return sum;
}
console.log(betterThreesFives(1, 12));