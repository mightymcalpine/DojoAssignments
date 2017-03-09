var arr = [5, 6]

function printReturn(arg1) {
	// console.log(arr[0]); 
	return arg1[1];
}
printReturn(arr);

console.log(arr[0]);
console.log(printReturn(arr))

// the function 'printReturn' returns the value of the second element of the array

// I noticed if I logged arr[0] within the function, the programe works but it results
// in arr[0] being printed twice, because I called the function twice,