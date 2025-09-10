# NumberGuessing
Number Guessing Game in Python

A simple Number Guessing Game built in Python, where the computer randomly picks a number between 1 and 100, and the player has to guess it within a limited number of attempts.

This project showcases the use of functions, recursion, error handling, and user input validation in Python.

Features:
* Random Number Generation – The computer selects a random number between 1–100 each game.
* Difficulty Levels
    - Easy Mode → 10 attempts
    - Hard Mode → 5 attempts
* Input Validation
    - Ensures only valid integers are accepted.
    - Rejects invalid input gracefully with retry prompts.
* Game Feedback
    - Provides hints: “Too high” or “Too low” after each guess.
* Life System
    - Tracks remaining attempts and ends the game when lives run out.
* Replay Option
    - After a game ends, players can choose to play again without restarting the script.
* ASCII Art Integration
    - A simple logo is displayed at the start of the game (via art.py).

Technologies Used
* Python 3
* random module for number generation
* Custom ASCII art (from art.py)

Project Structure
<pre>
📁 number-guessing-game
│── main.py      # Game logic
│── art.py       # ASCII art logo
│── README.md    # Project documentation
</pre>

How to Run
1. Clone this repository:
    - git clone https://github.com/<your-username>/number-guessing-game.git
    - cd number-guessing-game
2. Run the game
    - python main.py

Sample Gameplay:
<pre>
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': hard

You have 5 attempts remaining to guess the number.
Make a guess: 50
Too low.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess: 75
Too high.
Guess again.
...
You got it! The answer was 68.
</pre>

Future Enhancements:
* Add a leaderboard to track best scores.
* Allow custom difficulty levels (e.g., user-defined attempt count).
* Expand number range dynamically.
* GUI version with Tkinter or PyGame.