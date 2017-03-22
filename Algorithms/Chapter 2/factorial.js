var product = 1;
function factorial(num) {
	while (num > 0) {
		product *= num;
		num--;
	}
	return product;
}
console.log(factorial(5));