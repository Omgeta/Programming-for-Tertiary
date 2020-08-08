# Hangman SP

Hangman project for Singapore Polytechnic CA2.

Designed and implemented by @Omgeta in JavaScript.


# Overview

Hangman is a classic word game in which a computer randomly selects a word that the player must guess by supplying each of its letter: for each incorrect guess, a part of a stick figure of a hanged man is drawn. The player loses when the complete hanged man is drawn.


# Requirements

- There must be at least 40 words in a pool. 
- All words must be stored in an array. 
- The program randomly selects 10 words from the pool for each gameplay. 
- The game is over either when the user wins by correctly guessing all 10 words or loses when all parts of the hangman is drawn. 
- There must be at least 3 lifelines for each gameplay. They are (1) show all vowels, (2) show definition of the word, and (3) allow user to score and move on to the next word. Note that player will not be allowed to use lifeline (1) if all vowels are already shown and player is given only 1 of each lifeline per gameplay. 
- The program must be able to track the scores of each gameplay. The player scores when he/she guesses a word correctly.
- When the game is over, the result screen that shows the player’s score must be displayed. A congratulation message should be displayed if the player manages to guess all words correctly.

### You are to develop the application using the object oriented concept learnt in the module. Your application should consist of at least 2 of these classes i.e.

- ***Word*** class to define each word in the game (along with other attribute(s) such as its definition). 
- ***WordCollection*** class to represent a collection (pool) of all words. All required functions, such as a function to randomly select words from the pool for each gameplay, a function to check if the word is guessed correctly by player, a function to keep track of the score, etc. should also be included here.
- Feel free to add any other classes you feel are needed in your program. 

### Marks will be awarded for advanced features, such as, but not limited to the following:

- All words are stored in an external file (e.g. CSV file or TXT file) or database. 
- There are categories of words for player to choose at the beginning of each game. For example, IT Related, Geography, Biology, etc. The game then randomly picks the words from the selected category from the word pool. 
- The player can choose to display statistics such as his/her average score, highest score or lowest score, elapse time, etc. 
- The program is able to keep track of player’s scores (the scores and player info must be stored in an external file or database). 
- Any other features advanced features ie no in basic requirements above. 

Please keep in mind that all these are advanced features. The main bulk of marks are allocated to the completion of a workable program that meets the minimum requirements.

**You should try to fulfil the minimum requirements before you attempt the advanced features**

# Comments



