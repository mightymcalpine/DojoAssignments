// function findMax(arr) {
// 	var max = Math.max(...arr);
// 	return max;
// }
// findMax([1, 4, 5, 29, 79, 3, 100]);

// function findMax(arr) {
// 	return Math.findMax.apply(null, arr);
// }
// findMax([1, 4, 5, 29, 79, 3, 100]);


// var arr = Math.max(1, 5, 87, 3);
// console.log(arr);

// function getMaxOfArray(numArray) {
//   return Math.max.apply(null, numArray);
// }
// getMaxOfArray([1, 5, 87, 3]);

function findMax(arr) {
    var max = arr[0];
    for(var i = 1; i < arr.length; i++) {
        if (max < arr[i]) {
            max = arr[i]
        }
    }
    return max; 
}
findMax([1, 5, 87, 3]);