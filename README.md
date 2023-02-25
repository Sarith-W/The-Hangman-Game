# The-Hangman-Game
This contains the code and the test report for a single player game called "Hangman".

This is a single player game. A player is presented with some empty spaces to guess a word. Player will have limited number of guesses (known as turns). The initial number of turns are equal to the number of characters in the word. For example, if the word is “Potato”, the number of turns is 6. The player can win the game by guessing the correct word within the given turns. The game will end based on below scenarios.

Scenario 1
Player guesses the correct word within the given number of turns. The result - Player wins.

Scenario 2
Player runs out of turns before guessing the word. The result – Player loses.

If the player guesses a character properly, his/her turn will not exhaust. Only the wrong guesses will exhaust turns. If the word consists of duplicate characters, a single guess will fill all the occurrence of that letter.
For example, if the hidden word is “banana” and the player guesses the character “a”. This will show the filled guesses as “_ a _ a _ a” revealing all 3 positions of the letter “a”.

The program have 20 stored words which will randomly appear during the game. All 20 words have different number of turns based on the word size. As an addition it displays a small hint for the player about the word. The program also collect the player information and keep records of the games played. The collected information contains,
• Player’s name
• Word guessed
• Turns provided
• Turns used
• Win/lost status
