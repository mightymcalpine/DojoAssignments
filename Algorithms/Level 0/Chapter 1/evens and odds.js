var testArr = [5, 6, 4, 8, 7, 3, 3, 11, 1984, 91, 1555, 39, 6, 3, 84, 88, 86, 5, 8, 13, 711, 1091, 626];
var testArr2 = [1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2]

var threeOdds = 0;
var threeEvens = 0;

function evensOdds(arr) {
	for (var x = 0; x < arr.length; x++) {
		if (arr[x] % 2 !== 0) { // odd
			threeOdds++;
			threeEvens = 0;
			if (threeOdds == 3) {
				console.log("That's odd!");
			}
		}
		if (arr[x] % 2 == 0) { // even
			threeEvens++;
			threeOdds = 0;
			if (threeEvens == 3) {
				console.log("Even more so!")
			}
		}
	}
}
evensOdds(testArr2);