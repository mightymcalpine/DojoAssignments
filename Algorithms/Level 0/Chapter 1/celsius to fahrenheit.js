//  This program converts Celsius to Fahrenheit

function celsiusToFahrenheit(cDegrees) {
	var fahrenheit = (((cDegrees * 9) / 5) + 32);
	return fahrenheit;
}
celsiusToFahrenheit(-1);

// 		***** Optional Challenge *****


// This program will determine if Fahrenheit and Celsius equate at any point
// between 200 and -200 degrees 

function fahrenheitCelsiusEquate(arg1) {
	for (var x = 200; x > arg1; x--) {
		var fahrenheit = (((x * 9) / 5) + 32);
		if (x == fahrenheit) {
			console.log("At", x, "Fahrenheit and Celsius equate");
		}
	}
	return x;
}
fahrenheitCelsiusEquate(-200);