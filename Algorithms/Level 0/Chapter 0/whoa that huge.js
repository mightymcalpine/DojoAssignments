var sum = 0;
for (var x = -300000; x <= 300000 ; x++) {
	if (x % 2 != 0) {
		sum += x;
	}
}
console.log(sum);