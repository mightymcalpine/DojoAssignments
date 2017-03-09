// if arr[0] > arr.length --> "Too Big!"
// if arr[0] < arr.length --> "Too Small"
// if arr[0] == arr.length --> "Just Right"

var testArr = [3, 3, 1];

function fitFirstValue(arr) {
	if (arr[0] > arr.length) {
		console.log("Too Big!")
	}
	else if (arr[0] < arr.length) {
		console.log("Too Small")
	}
	else if (arr[0] == arr.length) {
		console.log("Just Right")
	}
}
fitFirstValue(testArr);