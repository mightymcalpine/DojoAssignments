var x = 0;
while (x <= 60000) {
	if (x % 6 == 0) {
		console.log(x);
	}
	x++;
	// x += 6;
}

// based on the wording of the challenge, I already know my output will be every 6th
// number, so my program would be faster and use less memory if I incremented with
// x += 6, I could also eliminate line 3

// However, if I needed to check every number from 0 to 60000 for some reason,
// I would just use x++, either way for this specific challenge, the result is the same

// ** view of console output is limited