/*
Author: Omgeta
Date: 4/8/2020
Description: Hangman Game
*/

// Dependencies
const fs = require("fs");
const readlineSync = require("readline-sync");

// Externals
const { WordCollection } = require("./hangman.js");
const wordlists = fs.readdirSync("./wordlists/").filter(file => file.endsWith(".csv"));
function wordlistsString() {
	return wordlists.map(e => e.split(".").slice(0, -1).join(".").toUpperCase()).join(", ");
}

// Name
const name = readlineSync.question("Enter your name: ").trim();

// Main
let running = true;
while (running) {
	// Choose wordlist
	const category = readlineSync.question(`Pick a wordlist (${wordlistsString()}): `).trim().toLowerCase();
	const wordlist = wordlists.find(e => e == category.concat(".csv"));
	if (!wordlist) continue;
	const game = new WordCollection("./wordlists/".concat(wordlist));

	// Game
	game.start(name);
	while (!game.winner) {
		game.display();
		const input = game.prompt();
		game.update(input);
	}
	game.win();

	// Restart prompt
	const restart = readlineSync.question("Would you like to try again (Y/N): ").trim().charAt(0).toUpperCase();
	if (!restart == "Y") {
		running = false;
	}
}
