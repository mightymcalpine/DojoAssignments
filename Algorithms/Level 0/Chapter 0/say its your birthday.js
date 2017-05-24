function birthday(day, month) {
	if (day == 25 && month == 4) {
		console.log('How did you know?');
	}
	else if (day == 4 && month == 25) {
		console.log('How did you know?');
	}
	else {
		console.log('Just another day....');
	}
}
birthday(25, 4);
birthday(4, 25);
birthday(3, 15); // just some numbers that are not my birthday