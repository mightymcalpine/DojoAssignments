// Remove Shorter Strings

var length = 22;
var manyStr = [
	'luke skywalker jedi knight',
	'darth sidious dark lord of the sith',
	'little green yoda grand master of the jedi',
	'mace windu',
	'force power rising'	
]
function removeShorter(manyStr, length) {
	var newArr = [];
}
for (var str = 0; str < manyStr.length; str++) {
	if (manyStr[str].length >= length) {
		
	};
};
console.log(manyStr);

// String: Reverse

var hero = 'skywalker'
function reverseString(str) {	
	var newStr = '';
	for (var idx = str.length - 1; idx >= 0; idx--) {
		newStr += str[idx];
	}
	return newStr
}
console.log(reverseString(hero));