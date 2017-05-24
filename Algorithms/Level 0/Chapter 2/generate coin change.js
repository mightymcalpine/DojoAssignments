function generateCoinChange(cents) {
	var dollar = cents % 100;
	var numOfDollars = (cents - dollar) / 100;
	console.log('dollars: ' + numOfDollars);
	var halfDollar = dollar % 50;
	var numOfHalfDollars = (dollar - halfDollar) / 50;	
	console.log('half dollars: ' + numOfHalfDollars);
	var quarters = halfDollar % 25;
	var numOfQuarters = (halfDollar - quarters) / 25;
	console.log('quarters: ' + numOfQuarters);
	var dimes = quarters % 10;
	var numOfDimes = (quarters - dimes) / 10;
	console.log('dimes: ' + numOfDimes);
	var nickles =  dimes % 5;
	var numOfNickles = (dimes - nickles) / 5;
	console.log('nickles: ' + numOfNickles);
	var numOfPennies = (nickles);  
	console.log('pennies: ' + numOfPennies);
}
generateCoinChange(136);