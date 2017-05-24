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
			runner.nextNode = newNode
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
		var runner = this.head
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
	this.minMaxAvg = function(){
		// console.log(this.length())
		if (!this.head) {
			return null
		}				
		if (this.length() == 1) {
			return 'There is only one node in the list'
		}
		var runner = this.head.nextNode
		if (runner) {
			var max = min = sum = this.head.value		 		
			while	(runner) {
				if (runner.value > max) {
					max = runner.value
				}
				if (runner.value < min) {
					min = runner.value
				}
				sum += runner.value
				runner = runner.nextNode
			}
			var avg = sum / this.length()
			return 'The max is: ' + max + ', The min is: ' + min + ', The avgerag is: ' + avg
		}
	}
}

function addToBack(list, node) {
	var runner = list.head
	if (!runner) {
		list.head = node
	}
	else {
		while(runner.nextNode){
			runner = runner.nextNode
		}
		runner.nextNode = node
	}
	return list
}
// node constructor
function listNode(val) {
	this.value = val;
	this.nextNode = null;
}


var ourList = new sList()
var nodeOne = new listNode(1)
var nodeTwo = new listNode(2)
var nodeThree = new listNode(3)

addToBack(ourList, nodeOne)
addToBack(ourList, nodeTwo)
addToBack(ourList, nodeThree)

ourList.addToBack(4).addToBack(5).addToBack(6)
// ourList.removeFront()
// console.log(ourList);
// console.log(ourList.head);
// console.log(ourList.length());
ourList.display();
console.log(ourList.minMaxAvg())


