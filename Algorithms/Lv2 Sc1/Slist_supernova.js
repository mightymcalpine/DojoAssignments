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
	this.removeFromBack = function() {
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
	this.addFront = function(val){
		var newNode = new listNode(val)
		newNode.nextNode = this.head
		this.head = newNode
		return this
	}
	this.removeFront = function(){
		if (!this.head) {
			return null
		}
		var temp = this.head.value
		this.head = this.head.nextNode
		return temp
	}
	this.front = function(){
		if (!this.head) {
			return null
		}
		return this.head.value
	}
	this.contains = function(val){
		var runner = this .head
		while(runner){
			if(runner.value == val){
				return true
			}
			runner = runner.nextNode
		}
		return false
	}
	this.length = function(){
		var count = 0
		var runner = this.head
		while(runner){
			count++
			runner = runner.nextNode
		}
		return count
	}
	this.display = function(){
		runner = this.head
		while(runner){
			if (runner.nextNode) {
			console.log('listNode { value: '+ runner.value + ', nextNode: '+ runner.nextNode.value + ' }')
			}
			else{
				console.log('listNode { value: '+ runner.value + ', nextNode: '+ runner.nextNode + ' }')	
			}
			runner = runner.nextNode
		}
		return
	}
	
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


function listNode(val) {
	this.value = null;
	this.next = val;
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
