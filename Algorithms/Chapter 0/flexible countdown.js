function flexCount(l, h, m) {
	for (var x = h; x >= l; x--) {
		if (x % m == 0) {
			console.log(x);
		}
	}
}
flexCount(2, 9, 3)
flexCount(10, 100, 10)