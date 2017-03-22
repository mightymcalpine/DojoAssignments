var dayUntilMyBirthday = 31;

function birthdayCountDown(days) {
	while (days >= 0) {
		if (days >= 30) {
			console.log(days + ' days until my birthday. Such a long time... :(');
		}
		else if (days < 30 && days > 4) {
			console.log(days + ' days until my birthday. Excitement rising ^^^^^');
		}
		else if (days <= 4 && days >= 1) {
			console.log('JUST ' + days + ' DAYS TO GO! SO CLOSE!')
		}
		else if (days == 0) {
			console.log('HAPPY BIRTHDAY TO ME!')
			break;
		}
		days--;
	}
}
birthdayCountDown(dayUntilMyBirthday);