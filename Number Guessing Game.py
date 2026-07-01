import random
import time

# High score untuk setiap level
high_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}


def get_difficulty():
    while True:
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")

        choice = input("Enter your choice: ")

        if choice == "1":
            return "Easy", 10
        elif choice == "2":
            return "Medium", 5
        elif choice == "3":
            return "Hard", 3
        else:
            print("Invalid choice. Please try again.")


def play_game():
    print("\n===================================")
    print("Welcome to the Number Guessing Game!")
    print("===================================")
    print("I'm thinking of a number between 1 and 100.")

    difficulty, chances = get_difficulty()

    print(f"\nGreat! You have selected the {difficulty} difficulty level.")
    print("Let's start the game!")

    secret_number = random.randint(1, 100)
    attempts = 0

    start_time = time.time()

    while attempts < chances:
        try:
            guess = int(input(f"\nEnter your guess ({attempts+1}/{chances}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            end_time = time.time()
            elapsed = round(end_time - start_time, 2)

            print("\n🎉 Congratulations!")
            print(f"You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {elapsed} seconds.")

            # Update High Score
            if (high_scores[difficulty] is None or
                    attempts < high_scores[difficulty]):
                high_scores[difficulty] = attempts
                print("🏆 New High Score!")

            return

        elif guess > secret_number:
            print("Incorrect! The number is less than", guess)
        else:
            print("Incorrect! The number is greater than", guess)

        # Hint System
        remaining = chances - attempts

        if remaining == 1:
            if secret_number % 2 == 0:
                print("Hint: The number is EVEN.")
            else:
                print("Hint: The number is ODD.")

            if secret_number > 50:
                print("Hint: The number is greater than 50.")
            else:
                print("Hint: The number is 50 or less.")

    print("\nGame Over!")
    print(f"The correct number was {secret_number}.")


def show_high_scores():
    print("\n====== HIGH SCORES ======")
    for level, score in high_scores.items():
        if score is None:
            print(f"{level}: No score yet")
        else:
            print(f"{level}: {score} attempts")
    print("=========================")


def main():
    while True:
        play_game()

        show_high_scores()

        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != "y":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()