var testScore = 52;
var grade;

function letterGrade(score) {
	if (score >= 90 && score <= 100) {
		grade = 'A';
	}
	if (score >= 80 && score <= 89) {
		grade = 'B';
	}
	if (score >= 70 && score <= 79) {
		grade = 'C';
	}
	if (score >= 60 && score <= 69) {
		grade = 'D';
	}
	else {
		grade = 'F';
	}
	return 'Score: ' + testScore + ' Grade: ' + grade;
}
console.log(letterGrade(testScore));