var hour;
var minutes;
var period;

function whatTime(hour, minutes, period) {
	if (hour < 12) {	
	}
	if (minutes == 15) {
		minutes = "quarter after";
	}
	else if (minutes < 30) {
		minutes = 'just after';
	}
	else if (minutes == 45) {
		minutes = "quarter until";
		if (hour != 12) {
		hour++;
		}
		else {
			hour = 1;
		}
	}
	else if (minutes < 60) {
		minutes = 'almost';
		if (hour != 12) {
		hour++;
		}
		else {
			hour = 1;
		}
	}
	if (period == 'am') {
		period = 'in the morning';
	}
	else if (period == 'pm') {
		period = 'in the evening';
	}
	return "It's " + minutes + ' ' + hour + ' ' + period;
}
console.log(whatTime(12, 45, 'pm'));
