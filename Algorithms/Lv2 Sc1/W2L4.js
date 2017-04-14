// list constructor
function sList() {
	this.head = null;
	this.addToBack = function(val){
		var runner = this.head
		var newNode = new listNode(val)
		if (!runner) {
			this.head = newNode
		}
		else {
			while(runner.nextNode){
				runner = runner.nextNode
			}
			runner.next = newNode
		}
		return this
	}
}

// node constructor
function listNode(val) {
	this.value = null;
	this.next = val;
}

function addToBack(val) {
	var runner = this.head
	if (!runner) {
		this.head = node
	}
	else {
		while(runner.nextNode){
			runner = runner.nextNode
		}
		runner.next = node
	}
	return list
}

// removing nodes
function removeFromBack(list) {
	var runner = this.head
 	if(!runner || !runner.nextNode){
		list.head = null
	}
	else {
		while (runner.nextNode.nextNode) {
			runner = runner.nextNode
		}
		runner.nextNode = null
	}
	return list
}

var ourList = new sList()
var nodeOne = new listNode(5)
var nodeTwo = new listNode(10)
var nodeThree = new listNode(15)

addToBack(ourList, nodeOne)
addToBack(ourList, nodeTwo)
addToBack(ourList, nodeThree)

ourList.addToBack(20)
console.log(ourList);
console.log(ourList.head);
