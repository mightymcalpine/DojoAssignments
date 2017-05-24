//  You are given two numbers – the coefficients M and B in the equation Y = MX + B
// 	 Build a function that returns the X-intercept
// 	the X-intercept is the value of X where Y equals zero

function mathHelp(m, b) {
	var x = -b/m;
	return x;
}
console.log(mathHelp(2, 2));