function whatReallyHappened() {
	var died = false;
	// 10% chance of death by volcano (1 - 10)
	var randomNum = Math.floor((Math.random() * 100) + 1);
	if (randomNum <= 10) {
		console.log("Kenny was volcano'd to death");
		died = true;
	}
	// 15% chance of death by tsunami (11 - 25)	
	randomNum = Math.floor((Math.random() * 100) + 1);
	if (randomNum <= 25) {
		console.log("Kenny was tsunami'd to death");
		died = true;	
	}	
	// 20% chance of death by earthquake (26 - 45)
	randomNum = Math.floor((Math.random() * 100) + 1);
	if (randomNum <= 45) {
		console.log("Kenny was earthquake'd to death");
		died = true;
	}
	// 25% chance of death by blizzard (46 - 70)
	randomNum = Math.floor((Math.random() * 100) + 1);
	if (randomNum <= 70) {
		console.log("Kenny was blizzard'd to death");
		died = true;
	}
	// 30% chance of death by meteor strike (70 - 100)
	randomNum = Math.floor((Math.random() * 100) + 1);
	if (randomNum <= 100) {
		console.log("Kenny was meteor'd to death");
		died = true;
	}
	if (died = false) {
		console.log("Kenny is ALIVE!");
	}
}
whatReallyHappened();

