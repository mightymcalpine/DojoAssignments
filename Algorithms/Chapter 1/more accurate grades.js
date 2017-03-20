var testScore = 49;
var grade, sign = '';

function accuGrader(score) {
	if (score >= 90 && score <= 100) {
		grade = 'A';
	}
	else if (score >= 80 && score <= 89) {
		grade = 'B';
	}
	else if (score >= 70 && score <= 79) {
		grade = 'C';
	}
	else if (score >= 60 && score <= 69) {
		grade = 'D';
	}
	else {
		grade = 'F';
	}
	if (grade == 'A') {
		if (score % 10 <= 2) {
			sign = '-';
		}
	}	
	if (grade != 'A' && grade != 'F') {
		if (score % 10 <= 2) {
		sign = '-';
		}
		else if (score % 10 >= 8) {
			sign = '+';
		}
	}
	return 'Score: ' + testScore + ',' + ' Grade: ' + grade + sign;
}
console.log(accuGrader(testScore));