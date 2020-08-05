/*
Author: Omgeta
Date: 4/8/2020
Description: Hangman Game
*/

const fs = require("fs");
const readlineSync = require("readline-sync");

const { WordCollection } = require("./hangman.js");
const wordlists = fs.readdirSync("./wordlists").filter(file => file.endsWith(".csv"));
function wordlistsString() {
	return wordlists.map(e => e.split(".").slice(0, -1).join(".").toUpperCase()).join(", ");
}

const name = readlineSync.question("Enter your name: ").trim();
let running = true;
while (running) {
	const category = readlineSync.question(`Pick a wordlist (${wordlistsString()}): `).trim().toLowerCase();
	const wordlist = wordlists.find(e => e == category.concat(".csv"));
	if (!wordlist) continue;
	const game = new WordCollection("./wordlists".concat(wordlist));

	game.start(name);
	while (!game.winner) {
		game.display();
		const input = game.prompt();
		game.update(input);
		game.nextRound();
	}
	game.win();

	const restart = readlineSync.question("Would you like to try again (Y/N): ").trim().charAt(0).toUpperCase();
	if (!restart == "Y") {
		running = false;
	}
}
