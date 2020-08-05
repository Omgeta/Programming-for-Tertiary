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
		this.lifelines = [1, 2, 3];
		this.winner = null;
	}

	getWordList() {
		return this.words;
	}

	getCurrentWord() {
		return this.currentWord;
	}

	getLifelines() {
		return this.lifelines;
	}

	getGameWords() {
		return this.gameWords;
	}

	getRounds() {
		return [this.round, this.gameWords.length];
	}

	getScore() {
		return this.score;
	}

	generateRandomSet(n) {
		/* Generate random array of n words from words array */
		const fullSet = this.getWordList().slice();
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
		for (const char of "aieou") {
			this.updateHidden(char);
		}
	}

	useLifeline(input) {
		/* Use lifeline and delete it from available lifelines */
		switch (input) {
			case 1:
				this.showAllVowels();
				break;
			case 2:
				console.log(`Description of the word is ${this.getCurrentWord().getDefinition()}`);
				break;
			case 3:
				this.correctWord();
				break;
		}
		const i = this.getLifelines().indexOf(input);
		this.lifelines.splice(i, 1);
	}

	updateHidden(replacement) {
		/* Replace characters on player's string if they are also found on the word */
		const word = this.getCurrentWord();
		for (let i = 0; i < word.getWord().length; i++) {
			if (word.getWord()[i] == replacement) {
				word.hidden = word.hidden.slice(0, i) + replacement + word.hidden.slice(i + 1);
				word.alphabet.replace(replacement, " ");
			}
		}
	}

	guess(char) {
		/* Guess character of word */
		const word = this.getCurrentWord();
		if (word.getWord().includes(char)) {
			this.updateHidden(char);
		} else {
			word.failedGuesses++;
		}
	}

	evaluate() {
		/* Return true if player's string is the same as the actual word */
		const word = this.getCurrentWord();
		return word.getWord() == word.getHidden();
	}

	correctWord() {
		/* Score points and go to next word */
		this.score++;
		this.nextRound();
	}

	nextRound() {
		/* Go to next word, or if at end of list then end game */
		if (this.round < this.gameWords.length) {
			this.round++;
			this.currentWord = this.gameWords[this.round - 1];
		} else {
			this.winner = this.player;
		}
	}

	log(newName, newScore) {
		/* Log score to logs.csv */
		const data = {};
		for (const line of fs.readFileSync("log.csv").split("\n")) {
			const [ name, score ] = line.split(",");
			data[name] = score;
		}

		if (newName in data) {
			data[newName] += newScore;
		} else {
			data[newName] = newScore;
		}

		const r = "";
		for (const name in data) {
			r.concat(`${name},${data[name]}\n`);
		}

		fs.writeFileSync("log.csv", r, "utf-8");
	}

	start(name) {
		/* Initialise variabes */
		this.player = name;
		this.gameWords = this.generateRandomSet(10);
		this.round = 1;
		this.score = 0;
		this.currentWord = this.gameWords[0];
	}

	display() {
		/* Graphically display current hangman, current player's string and letters left to guess */
		const insertSpacesBetween = (string) => {
			let result = "";
			for (let i = 1; i < string; i += 2) {
				result = string.slice(0, i) + " " + string.slice(i);
			}
			return result;
		};

		/*
		const getHangman = (failedGuesses) => {
			// I am way too lazy to do ASCII art
		};
		*/

		const currentWord = this.getCurrentWord();
		// console.log(getHangman(currentWord.getFailedGuesses()));
		if (currentWord.getFailedGuesses() >= 8) {
			console.log("Oh no, you died of failing too many times! Try the next word.");
			this.nextRound();
		}
		console.log(insertSpacesBetween(currentWord.getHidden()));
		console.log(insertSpacesBetween(currentWord.getAlphabet()));
	}

	prompt() {
		/* Prompt player for input and validate */
		const isAlpha = (string) => {
			return string.match(/^[A-Za-z]+$/);
		};

		const isNumber = (string) => {
			return string.match(/^[0-9]+$/);
		};

		const lifelineString = () => {
			const lifelineDescriptions = {
				1: "Show all vowels",
				2: "Show definition of word",
				3: "Skip and get correct",
			};

			const result = this.getLifelines().map(x => lifelineDescriptions[x]);
			return result.join(", ");
		};

		const unusedLifeline = (lifeline) => {
			return this.getLifelines().includes(lifeline);
		};

		const notGuessed = (char) => {
			const word = this.getCurrentWord();
			return word.getAlphabet().includes(char);
		};


		while (true) {
			let input = readlineSync.question(`${this.name}'s guess (Enter 9 for lifelines or 0 to pass): `).trim().charAt(0);
			if (isAlpha(input)) {
				if (notGuessed(input)) {
					return input;
				} else {
					console.log("Letter has already been guessed! Try again.");
				}
			} else if (isNumber(input)) {
				if (input == "0") {
					return input;
				} else if (input == "9") {
					if (this.lifelines) {
						input = readlineSync.question(`Use one of your lifelines (${lifelineString()})`).trim().charAt(0);
						if (isNumber(input) && unusedLifeline(input)) {
							return input;
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
			this.nextRound();
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
		console.log(`Results==========\nName:${this.getName()}\nScore:${this.score}/${this.getGameWords().length}`);
		this.log(this.player, this.score);
	}
}

class Word {
	constructor(word, definition) {
		this.word = word;
		this.definition = definition;
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

	hiddenHasVowels() {
		for (const char of this.word) {
			if ("aeiou".includes(char) && !this.hidden.includes(char)) {
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
