var testArr = ['James', 'Jill', 'Jane', 'Jack'];

function fancyArray(arr) {
	for (var x = 0; x < arr.length; x++) {
		console.log(arr[x] = x + ' -> ' + arr[x]);
	}
}
fancyArray(testArr);

