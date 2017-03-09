function leapYear(year) {
	if (year % 4 == 0) {
		if (year % 400 != 0) {
			if (year % 100 != 0) {
				console.log(year, 'is a leap year!');
			}
			else {
				console.log(year, 'is NOT a leap year!')
			}
		}
		else {
			console.log(year, 'is a leap year!');
		}
	}
	else {
		console.log(year, 'is NOT a leap year!');
	}
}
leapYear(2016);
leapYear(2000);
leapYear(1900);
leapYear(1957);
leapYear(2020);
leapYear(2024);
leapYear(1946);