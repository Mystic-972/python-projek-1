# Number Guessing Game

A simple Command Line Interface (CLI) Number Guessing Game built with Python.

## Description

The computer randomly selects a number between **1 and 100**.

The player chooses a difficulty level and tries to guess the number before running out of chances.

After every incorrect guess, the game tells the player whether the secret number is higher or lower.

## Features

- Random number generation (1-100)
- Three difficulty levels
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- Higher/Lower hints
- Input validation
- Timer
- High score tracking
- Play multiple rounds

## 🛠 Requirements

- Python 3.x

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/number-guessing-game.git
```

Go to the project directory:

```bash
cd number-guessing-game
```

Run the game:

```bash
python number_guessing_game.py
```

or

```bash
python3 number_guessing_game.py
```

## Gameplay

1. Select a difficulty level.
2. Enter your guesses.
3. The game will tell you whether the secret number is higher or lower.
4. Win before your chances run out!

## Sample Output

```text
Welcome to the Number Guessing Game!

Please select the difficulty level:

1. Easy
2. Medium
3. Hard

Enter your choice: 2

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Congratulations!
You guessed the correct number in 4 attempts.
```

## Author

Mystic

## Project URL

https://roadmap.sh/projects/number-guessing-game