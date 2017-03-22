function drawLeftStars(num, char) {
	var result = '';
	num = Math.abs(num) > 75 ? 75 : Math.abs(num);
	
	for (var x = 0; x < num; x++) {
		result += char;
	}
	var remChar = 75 - num;
	for (var x = 0; x < remChar; x++) {
		result += ' ';
	}
	return result;	
}

function drawRightStarts(num, char) {
	var result = '';
	var remChar = 75 - num;
	num = Math.abs(num) > 75 ? 75 : Math.abs(num);
	for (var x = 0; x < remChar; x++) {
		result += ' ';
	}
	for (var x = 0; x < num; x++) {
		result += char;
	}
	return result;
}

function drawCenterStars(num, char) {
	num = Math.abs(num);
	num = num > 75 ? 75 : num;
	var leftSpaces = Math.floor((75 - num) / 2);
	var result = '';
	for (var x = 0; x < leftSpaces; x++) {
		result += ' ';
	}
	for (var x = 0; x < num; x++) {
		result += char;
	}
	var rightSpaces = 75 - num - leftSpaces;
	for (var x = 0; x < rightSpaces; x++) {
		result += ' ';
	}
	return result;
}

var starArt = {
	left: drawLeftStars,
	center: drawCenterStars,
	right: drawRightStarts
};

console.log(starArt.right(55, '@'));
console.log(starArt.left(45, '^'));
console.log(starArt.center(55, '#'));