function slotMachine(coins) {

	while (coins > 0) {		
		var randomNum = Math.floor((Math.random() * 100) + 1);		
		if (randomNum === 56) {
			var winnings = Math.floor((Math.random() * 51) + 50);						
			console.log('You won ' + winnings + ' coins');
			coins += winnings;
			console.log('Your warchest has ' + coins + ' coins');
		}
		else {
			coins--;
			console.log('You lost. Too bad huh? Want to play again?');
			console.log('You have ' + coins + ' left');			
		}
		if (coins === 0) {			
			return 0;
		}
	}
}
var warChest = 12;
// while (warChest) {
// 	slotMachine(warChest);
// }
slotMachine(warChest);