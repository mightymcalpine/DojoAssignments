// Node constructor function
function Node(val) {
	if (!(this instanceof Node)) {
		return new Node(val);
	}
	this.value = val;
	this.next = null;
};

// Slist constructor function
function Slist() {
	if(!(this instanceof Slist)) {
		return new Slist();
	}
	this.head = null;	
};
// Add method, prototype is an instance of Slist
Slist.prototype.add = function(node) {
	if (!(node instanceof Node)) {
		node = new Node(node);
	}
	node.next = this.head;
	this.head = node;
	return this;
};
// Length method
Slist.prototype.length = function () {
	var runner = this.head;
	var count = 0;
	while	(runner) {
		count++;
		runner = runner.next;
	}
	return count;
};
// Reverse method with newList
Slist.prototype.reverse = function() {
	var newList = new Slist();
	var runner = this.head;
	while (runner) {
		newList.add(runner.value)
		runner = runner.next;
	}
	this.head = newList.head;
	return this;
};
// Reverse method sans newList, reverse in place
Slist.prototype.reverse2 = function() {
	var current = this.head;
	var prev = null;
	var next = null;
	while (current) {
		next = current.next;
		current.next = prev;
		prev = current;
		current = next;
	}
	this.head = prev;
	return this;
};
// find k node from the end of the list
// issue with this version, if k = 1, you have to go through the list twice
Slist.prototype.kthlast = function(k) {
	var len = this.length();
	if (k > len || k <= 0) {
		return null;
	}
	var runner = this.head;
	len -= k;
	for (var idx = 0; idx < len; idx++) {
		runner = runner.next;
	}
	return runner.value;
};
// find k node from the end of the list, sans lenth() method
Slist.prototype.kthlast2 = function(k) {
	if (k <= 0) {
		return null;
	}
	var runner = this.head;
	while (runner && k) {
		k--;
		runner = runner.next;
	}
	if (k) {
		return null;
	}
	var follower = this.head;
	while (runner) {
		runner = runner.next;
		follower = follower.next;
	}
	return follower;
};
// is palindrone method with new data structure, the temp array
// CPU efficient, memory hog
Slist.prototype.ispalindrone = function() {
	if (!this.head) {
		return true;
	}
	var runner = this.head;
	var temp = [];
	while (runner) {
		temp.push(runner.value);
		runner = runner.netxt;
	}
	for (var idx = 0; idx < Math.floor(temp.length/2); idx++) {
		if (temp[idx] === temp[temp.length - idx - 1]) {
			continue;
		}
		return false;
	}
	return true;
};
// is palindron2 method
// version 2 is memory efficient
Slist.prototype.ispalindrone2 = function() {
	var runner = this.head;
	var midpoint = Math.floor(this.length()/2);
	var idx = 1;
	while (idx <= midpoint) {
		if (runner.value !== this.kthlast2(idx++).value) {
			return false;
		}
		runner = runner.next;
	}
	return true;
};














// ** for ispalindrone:
var list2 = new Slist();
var str1 = 'racecar';
str1.split('').forEach(function(char) {
	list2.add(char);
});

// ** for methods accepting integers:
// var newNode = new Node(2);
// Slist.add(5).add(new Node(10));
var list1 = new Slist();
for (var x = 0; x < 10; x++) {
	list1.add(x);
}

// ** TESTING METHODS:
// console.log(list1.head);
// console.log(list1.reverse().reverse2().head);
// console.log(list1.kthlast2(10));
// console.log(list2.head);
console.log(list2.ispalindrone2());










