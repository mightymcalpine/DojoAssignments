function arrStack(){
	var stack = []
	
	this.push = function (val) {
		stack[stack.length] = val
		console.log(stack)
		return this
	}
	this.pop = function () {
		var returned = stack[stack.length -1]
		stack.length = stack.length - 1
		return returned
	}
}


var newStack = new arrStack()

console.log(newStack);
newStack.push(4).push(5).push(6)
console.log(newStack.pop())
console.log(newStack.pop())

// left of at 26:50 of W4L3