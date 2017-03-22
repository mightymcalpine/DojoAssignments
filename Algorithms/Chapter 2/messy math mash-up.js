
//  sum =add all integers from 0 up to the given num
// 		except for....

// If current count (not num) is evenly divisible by 3, don't add to sum;
// 	use continue to skip to the next value of count;

// Otherwise, if current count is evenly divisible by 7,
// 	include it twice in sum instead of once;

// Regardless of the above, if the current count is exactly 1/3 of num, return -1 immediately


function messyMath(num) {
	var sum = 0;
	var thirdOfNum = (num / 3);
	for (var x = 0; x < num; x++) {		
		if (x % 3 == 0) {
			continue;
		}
		if (x % 7 == 0) {
			sum += x * 2;
		}
		if (x === thirdOfNum) {
			return -1;
		}
	}
	return sum;
}
console.log(messyMath(9));