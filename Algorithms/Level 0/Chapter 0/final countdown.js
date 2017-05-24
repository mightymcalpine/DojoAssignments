function finalCountDown(arg1, arg2, arg3, arg4) {
	var x = arg3;
	while (x >= arg2) {
		if (x % arg1 == 0) {
			if (x != arg4) {
				console.log(x);
			}
			else {
			}
		}
	x--;
	}	
}
finalCountDown(3, 5, 17, 9);
finalCountDown(10, 10, 100, 50)