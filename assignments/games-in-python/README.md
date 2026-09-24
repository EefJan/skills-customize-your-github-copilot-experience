
# 🎮 Hangman Game Challenge

## Overview

Build a classic Hangman game in Python using strings, loops, and user input. The game should let a player guess letters to reveal a hidden word before they run out of attempts.

## Learning Goals

- Practice string manipulation
- Use loops and conditionals effectively
- Work with random selection and user input
- Build a complete game flow with win/lose logic

## Project Requirements

Your game must:
- Randomly select a word from a predefined list
- Accept letter guesses from the player
- Display the current word progress using underscores and revealed letters (for example: _ _ _)
- Track remaining incorrect guesses
- End the game when the player guesses the word correctly or runs out of attempts
- Show a clear win or lose message at the end

## Suggested Workflow

1. Create a list of words and choose one at random
2. Display blanks for each letter in the word
3. Prompt the player for a guess
4. Update the revealed letters and remaining attempts
5. Repeat until the word is solved or the player loses

## Acceptance Criteria

- The game runs without errors
- The player can guess letters repeatedly
- The program correctly tracks guessed letters and remaining attempts
- The game ends with an appropriate success or failure message
- The output is easy to follow and user-friendly

## Stretch Ideas

- Add a replay option after each round
- Prevent duplicate guesses
- Show the guessed letters so far
- Add a difficulty level with different word lengths or attempt counts
