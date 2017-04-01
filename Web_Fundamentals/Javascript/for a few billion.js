function doubleOneCent() {
	var total = 0;
	var penny = 0;
	for (var x = 1; x <= 30 ; x++) {
		if (x == 1) {
			penny = 0.01;
			console.log(penny);
		}
		else {
			penny *= 2
			total += penny; 
			console.log(penny);
		}
	}
	return total;
}
console.log(doubleOneCent());