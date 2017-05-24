var myNum = 42;
var myName = 'Marty';
var temp = myNum;
// temporarily storing the value of myNum in temp
console.log(myNum, myName);

myNum = myName;
// myNum is no longer 42
console.log(myNum);

myNum = temp;
// restoring myNum to its original value of 42
// and assigning it to myName
myName = myNum;
console.log(myName);
