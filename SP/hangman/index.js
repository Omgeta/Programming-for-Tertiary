const {WordCollection} = require("./hangman.js")
const wordlist = "./words.txt"


let game = new WordCollection(wordlist)
game.start()
while (!game.winner) {
	game.display()
	let input = game.prompt()
	game.update(input)
	game.nextRound()
}
console.log("=======\nResults\n=======\nScore: "+game.score)
