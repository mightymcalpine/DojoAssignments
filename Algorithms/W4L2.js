function node(val) {
	this.value = val
	this.nextNode = null
}
function slQueue(){
	var head = null
	this.next = null
	this.enqueue = function (val) {
		var newnode = new node(val)
		if (head == null) {
			head = newnode
			tail = newnode
		}
		else {
			tail.nextNode = newnode
			tail = newnode
		}
		return this
	}
	this.dequeue = function(){
		if (head) {
			var temp = head.value
			if (head.nextNode == null) {
				head = tail = null
			}
			else {
				head = head.nextNode
			}
			return temp
		}
		return null
	}
}

var myQueue = new slQueue()
myQueue.enqueue(5)
myQueue.enqueue(10)
myQueue.enqueue(15)
console.log(myQueue.dequeue())
console.log(myQueue.front())