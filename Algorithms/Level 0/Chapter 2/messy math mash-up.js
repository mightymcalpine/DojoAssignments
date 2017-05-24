function messyMath(num) {
	var sum = 0;	
	for (var x = 0; x <= num; x++) {		
		if (num/3 === x) {
			return -1;
		}
		else if (x % 3 == 0) {
			continue;
		}
		else if (x % 7 == 0) {
			sum += x * 2;
		}
		else {
			sum += x;
		}
	}
	return sum;
}
console.log(messyMath(7));