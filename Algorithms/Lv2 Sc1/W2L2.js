ls1 = [6, 12, 15, 18, 21, 24, 30];
ls2 = ['mcfranklin', 'rocket', 'moon', 'catmouth'];
obj = {}

function zipArrays(ls1, ls2) {
	for (var idx = 0; idx < ls1.length; idx++) {
		obj[ls1[idx]] = ls2[idx];
		if (!obj[ls1[idx]]) {
			obj[ls1[idx]] = 'EMPTY'
		}
	}
	return obj
}
console.log(zipArrays(ls1, ls2))
