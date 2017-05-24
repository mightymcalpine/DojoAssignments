var arr = [-3, 6, 9, -12, 15, -91, 21, -21];

for (var x = 0; x < arr.length; x++) {
	if (arr[x] < 0) {
		arr[x] = 'Dojo';
	}	
}
console.log(arr);