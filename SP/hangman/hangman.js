const fs = require("fs")
const readlineSync = require("readline-sync")
const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class WordCollection {
	constructor(filename) {
		this.wordList = []
		let file = fs.readFileSync(filename, "utf-8").split("\n")
		for (let line of file) {
			let wordDefinition = line.split(": ")
			this.wordList.push(new Word(wordDefinition[0].toUpperCase(), wordDefinition[1]))
		}

		this.score = 0
		this.lifelines = ["1","2","3"]
	}

	getWordList() {
		return this.wordList
	}

	getCurrentWord() {
		return this.currentWord
	}

	getLifelines() {
		return this.lifelines
	}

	getRounds() {
		let currentRound = this.gameWords.indexOf(this.currentWord) + 1
		let allRounds = this.gameWords.length
		return [currentRound, allRounds]
	}

	generateRandomSet(num) {
		let randomSet = []
		for (let i=0; i<num; i++) {
			randomSet.push(this.wordList[Math.floor(Math.random() * this.wordList.length)])
		}
		return randomSet
	}

	showAllVowels() {
		const word = this.getCurrentWord()
		for (const vowel of "aieou") {
			if (word.getWord().includes(vowel)) {
				this.updateHidden(char)
			}
		}
	}

  lifeline(input) {
		if (input == 1) {
			this.showAllVowels()
		} else if (input == 2) {
			console.log(this.getCurrentWord().getDefinition())
		} else if (input == 3) {
			this.correctWord()
		}
		this.lifelines.pop(input-1)
	}

	updateHidden(char) {
		function replaceAt(string, index, char) {
			return string.substr(0, index) + char + this.substr(index + char.length)
		}

		const word = this.getCurrentWord()
		for (let i=0; i<word.length; i++) {
			if (word.charAt(i) == char) {
				word.hidden = replaceAt(word.hidden, i, char)
				word.alphabet.replace(char, " ")
			}
		}
	}

  	notGuessed(char) {
		const word = this.getCurrentWord()
		if (word.getAlphabet().includes(char) && !word.getHidden().includes(char)) {
			return true
		} else {
			return false
		}
	}

	guess(char) {
		const word = this.getCurrentWord()
		if (word.getWord().includes(char)) {
			this.updateHidden(char)
			console.log("Good job! "+char+" is one of the letters!")
		} else {
			word.guesses++
			console.log("Sorry. "+char+" is not part of the word.")
		}
	}

	evaluate() {
		const word = this.getCurrentWord()
		if (word.getWord() == word.getHidden()) {
			return true
		} else {
			return false
		}
	}

	correctWord() {
		this.score++
		this.nextRound()
	}

	nextRound() {
		const [currentRound, allRounds] = this.getRounds()
		console.log(currentRound, allRounds)
		if (currentRound < allRounds) {
			this.currentWord = this.gameWords[this.gameWords.indexOf(this.currentWord) + 1]
		} else {
			this.winner = this.name
		}
	}

	start() {
		this.name = readlineSync.question("Please enter your name: ")
		this.gameWords = this.generateRandomSet(10)
		this.currentWord = this.gameWords[0]
	}

	display() {
		let getHangman = (guesses) => {
			/*let guesses = this.getCurrentWord().getGuesses()*/
		}

	    const word = this.getCurrentWord()
		console.log(getHangman(word.getGuesses()))
		console.log(WordCollection.insertSpacesBetween(word.getHidden()))
		console.log(WordCollection.insertSpacesBetween(word.getAlphabet()))
	}

	prompt() {
	  let validInput = (input) => {
			if (this.notGuessed(input) || (input == "0")) {
				return true
			} else if (input == "9") {
				const lifelines = this.getLifelines()
				if (lifelines) {
					const lifelineOne = lifelines.includes(1) ? "(1) Show all vowels " : ""
					const lifelineTwo = lifelines.includes(2) ? "(2) Show definition of word " : ""
					const lifelineThree = lifelines.includes(3) ? "(3) Score and skip word " : ""
					input = readlineSync.question(lifelineOne+lifelineTwo+lifelineThree).charAt(0)
					if (lifelines.includes(input)) {
						if (input == "1" && !WordCollection.includesVowels(this.getCurrentWord().getHidden())) {
							return true
						} else {
							console.log("All vowels are already shown.")
						}
					} else {
							console.log("You do have any more of this lifeline.")
					}
				} else {
					console.log("You have no more lifelines.")
				}
			} else {
				console.log("Invalid input.")
			}
			return false
		}

		let input = ""
		while (!validInput(input)) {
			input = readlineSync.question(this.name+"\'s" + " guess (Enter 9 for lifelines or 0 to pass): ").charAt(0).toUpperCase()
		}
		return input
	}

	update(input) {
		if (input == "0") {
			this.nextRound()
		} else if (input == "1" || input == "2" || input == "3") {
			this.lifeline(input)
		} else {
			this.guess(input)
		}
		if (this.evaluate()) {
			this.correctWord()
		}
	}

  static includesVowels(string) {
		let count = 0
		for (const char of "aieou") {
			if (string.includes(char)) {
				count++
			}
		}
	    if (count == 4) {
	      return true
	    } else {
	      return false
	    }
	}

  static insertSpacesBetween(string) {
			let result = ""
      for (const char of string) result = result + char + " "
			return result.slice(0, -1)
	}
}

class Word {
	constructor(word, definition) {
		this.word = word
		this.definition = definition
		this.hidden = "_".repeat(this.word.length)
		this.alphabet = alphabet
		this.guesses = 0
	}

	getWord() {
		return this.word
	}

	getDefinition() {
		return this.definition
	}

	getHidden() {
		return this.hidden
	}

	getAlphabet() {
		return this.alphabet
	}

	getGuesses() {
		return this.guesses
	}
}

module.exports = {
  WordCollection,
  Word
}
