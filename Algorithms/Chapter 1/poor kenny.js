var randomNum = Math.floor((Math.random() * 100) + 1);

function whatHappensToday(num) {
	// 10% chance of volcano (1 - 10)
	if (num <= 10) {
		return(randomNum + " Kenny was volcano'd");
	}
	// 15% chance of tsunami (11 - 25)	
	else if (num <= 25) {
		return(randomNum + " Kenny was tsunami'd");
	}
	// 20% chance of earthquake (26 - 45)
	else if (num <= 45) {
		return(randomNum + " Kenny was earthquake'd");
	}
	// 25% chance of blizzard (46 - 70)
	else if (num <= 70) {
		return(randomNum + " Kenny was blizzard'd");
	}
	// 30% chance of meteor strike (70 - 100)
	else if (num <= 100) {
		return(randomNum + " Kenny was meteor'd");
	}
}
console.log(whatHappensToday(randomNum));