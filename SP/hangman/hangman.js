/*
Author: Omgeta
Date: 4/8/2020
Description: Hangman Classes
*/

const fs = require("fs");
const readlineSync = require("readline-sync");
const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

class WordCollection {
	constructor(filename) {
		this.words = [];
		for (const line of fs.readFileSync(filename, "utf-8").split("\n")) {
			const [ word, definition ] = line.split(",");
			this.words.push(new Word(word, definition));
		}
		this.player;
		this.gameWords;
		this.currentWord;
		this.round;
		this.score;
		this.lifelines = ["1", "2", "3"];
		this.winner = null;
	}

	getWordList() {
		return this.words;
	}

	getPlayer() {
		return this.player;
	}

	getGameWords() {
		return this.gameWords;
	}

	getCurrentWord() {
		return this.currentWord;
	}

	getRounds() {
		return [this.round, this.gameWords.length];
	}

	getScore() {
		return this.score;
	}

	getLifelines() {
		return this.lifelines;
	}

	generateRandomSet(n) {
		/* Generate random array of n words from words array */
		const fullSet = this.getWordList().slice(); // Copy array
		const randomSet = [];
		for (let i = 0; i < n; i++) {
			const j = Math.floor(Math.random() * fullSet.length);
			randomSet.push(fullSet[j]);
			fullSet.splice(j, 1);
		}
		return randomSet;
	}

	showAllVowels() {
		/* Guess all correct vowels */
		for (const char of "AEIOU") {
			this.updateHidden(char);
		}
	}

	useLifeline(input) {
		/* Use lifeline and delete it from available lifelines */
		switch (input) {
			case "1":
				this.showAllVowels();
				break;
			case "2":
				console.log(`Description of the word is: ${this.getCurrentWord().getDefinition()}`);
				break;
			case "3":
				this.correctWord();
				break;
		}
		const i = this.getLifelines().indexOf(input);
		this.lifelines.splice(i, 1);
	}

	lifelineString() {
		const lifelineDescriptions = {
			1: "(1) Show all vowels",
			2: "(2) Show definition of word",
			3: "(3) Skip and get correct",
		};

		const result = this.getLifelines().map(x => lifelineDescriptions[x]);
		return result.join(", ");
	}

	unusedLifeline(lifeline) {
		/* Check if lifeline is vailable */
		return this.getLifelines().includes(lifeline);
	};

	updateHidden(char) {
		/* Replace characters on player's string if they are also found on the word */
		const word = this.getCurrentWord();

		word.alphabet = word.alphabet.replace(char, " ");
		char = char.toUpperCase();
		if (word.getWord().includes(char)) {
			for (let i = 0; i < word.getWord().length; i++) {
				if (word.getWord()[i] == char) {
					word.hidden = word.hidden.slice(0, i) + char + word.hidden.slice(i + 1);
				}
			}
			console.log(`Good job! ${char} is one of the letters!`);
			return true;
		} else {
			console.log(`Sorry. ${char} is not part of the word.`);
			return false;
		}
	}

	guess(char) {
		/* Guess character of word */
		const word = this.getCurrentWord();
		if (!this.updateHidden(char)) {
			word.failedGuesses++;
		}
	}

	notGuessed(char) {
		/* Check if character has already been guessed */
		const word = this.getCurrentWord();
		return word.getAlphabet().includes(char);
	};

	evaluate() {
		/* Return true if player's string is the same as the actual word */
		const word = this.getCurrentWord();
		return word.getWord() == word.getHidden();
	}

	correctWord() {
		/* Score points and go to next word */
		this.score++;
		this.nextWord();
	}

	nextWord() {
		/* Go to next word, or if at end of list then end game */
		const [ curr, last ] = this.getRounds()
		if (curr < last) {
			this.round++;
			this.currentWord = this.gameWords[this.round - 1];
		} else {
			this.winner = this.player;
		}
	}

	log(newName, newScore) {
		/* Log score to logs.csv */
		const data = {};
		for (const line of fs.readFileSync("log.csv", "utf-8").split("\n")) {
			const [ name, score ] = line.split(",");
			data[name] = score;
		}

		if (newName in data) {
			data[newName] += newScore;
		} else {
			data[newName] = newScore;
		}

		let r = "";
		for (const name in data) {
			console.log(name, data[name])
			r = r.concat(`${name},${data[name]}\n`);
		}

		fs.writeFileSync("log.csv", r, "utf-8");
	}

	start(name) {
		/* Initialise variables */
		this.player = name;
		this.gameWords = this.generateRandomSet(10);
		this.round = 1;
		this.score = 0;
		this.currentWord = this.gameWords[0];
	}

	display() {
		/* Graphically display current hangman, current player's string and letters left to guess */
		function insertSpacesBetween(string) {
			let result = string.slice(); // Copy string
			for (let i = 1; i < result.length; i += 2) {
				result = result.slice(0, i) + " " + result.slice(i);
			}
			return result;
		}

		function getHangman(failedGuesses) {
			// I am way too lazy to do ASCII art
			return `Failed Guesses: ${failedGuesses}`;
		}

		function displayHangman(word) {
			const failedGuesses = word.getFailedGuesses();
			console.log(getHangman(failedGuesses));
		}

		function displayHidden(word) {
			const hidden = word.getHidden();
			console.log(insertSpacesBetween(hidden));
		}

		function displayAlphabet(word) {
			const alphabet = word.getAlphabet();
			console.log(insertSpacesBetween(alphabet));
		}

		console.log("============================================================");
		const currentWord = this.getCurrentWord();
		const [ curr, last ] = this.getRounds();
		console.log(`Round ${curr}/${last}`);

		displayHangman(currentWord);
		displayHidden(currentWord);
		displayAlphabet(currentWord);

		if (currentWord.getFailedGuesses() >= 8) {
			console.log("Oh no, you died of failing too many times! Try the next word.");
			this.nextWord();
		}
		console.log("============================================================");
	}

	prompt() {
		/* Prompt player for input and validate */
		function isAlpha(string) {
			return string.match(/^[A-Za-z]+$/);
		}

		function isNumber(string) {
			return string.match(/^[0-9]+$/);
		}

		while (true) {
			let input = readlineSync.question(`${this.player}'s guess (Enter 9 for lifelines or 0 to pass): `).trim().charAt(0);

			if (isAlpha(input)) {
				if (this.notGuessed(input)) {
					return input;
				} else {
					console.log("Letter has already been guessed! Try again.");
				}
			} else if (isNumber(input)) {
				if (input == "0") {
					return input;
				} else if (input == "9") {
					if (this.lifelines) {
						input = readlineSync.question(`Use one of your lifelines (${this.lifelineString()})`).trim().charAt(0);
						if (isNumber(input) && this.unusedLifeline(input)) {
							if (input == "1") {
								if (!this.getCurrentWord().hasAllVowels()) {
									return input;
								} else {
									console.log("All vowels are already shown.");
								}
							} else {
								return input;
							}
						} else {
							console.log("Invalid integer input. Select one of the available lifelines.");
						}
					} else {
						console.log("All lifelines have been used");
					}
				} else {
					console.log("Invalid integer input. Enter either alphabet, 0 or 9.");
				}
			} else {
				console.log("Invalid input type. Enter either alphabet, 0 or 9.");
			}
		}
	}

	update(input) {
		/* Handle player's action according to player input */
		if (input == "0") {
			this.nextWord();
		} else if (["1", "2", "3"].includes(input)) {
			this.useLifeline(input);
		} else {
			this.guess(input);
		}
		if (this.evaluate()) {
			this.correctWord();
		}
	}

	win() {
		/* End screen */
		console.log("=============================\nResults\n=============================");
		console.log(`Name:${this.getPlayer()}`);
		console.log(`Score:${this.getScore()}/${this.getGameWords().length}`);

		this.log(this.getPlayer(), this.getScore());
	}
}

class Word {
	constructor(word, definition) {
		this.word = word.toUpperCase();
		this.definition = definition.toUpperCase();
		this.hidden = "_".repeat(this.word.length);
		this.alphabet = alphabet;
		this.failedGuesses = 0;
	}

	getWord() {
		return this.word;
	}

	getDefinition() {
		return this.definition;
	}

	getHidden() {
		return this.hidden;
	}

	getAlphabet() {
		return this.alphabet;
	}

	getFailedGuesses() {
		return this.failedGuesses;
	}

	hasAllVowels() {
		for (const char of "AEIOU") {
			if (this.getWord().includes(char) && this.getAlphabet().includes(char)) {
				console.log(char)
				return false;
			}
		}
		return true;
	}
}

module.exports = {
  WordCollection,
  Word,
};
