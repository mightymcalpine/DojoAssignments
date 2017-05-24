var sum = 0;
function sigma(num) {
	while (num > 0) {
		sum += num;
		num--;
	}
	return sum;
}
console.log(sigma(6));