from art import logo
import random

# Display the logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number_random = random.randint(1, 100)


def check_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Set number of attempts based on the difficulty level
    if level == "hard":
        attempts = 5
    elif level == "easy":
        attempts = 10
    else:
        print("Invalid choice. Please choose 'easy' or 'hard'.")
        return check_difficulty()  # Retry if invalid input

    # Loop to allow guessing until attempts run out
    while attempts > 0:
        try:
            answer = int(input("Make a guess: "))  # Convert answer to integer
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts -= 1
        if answer > number_random:
            print("Too High.")
        elif answer < number_random:
            print("Too Low.")
        else:
            print(f"Congratulations! You guessed the right number: {number_random}")
            return

        print(f"You have {attempts} attempts remaining.")

    # If attempts run out, reveal the number
    print(f"Sorry, you're out of attempts. The number was {number_random}.")


# Start the game
check_difficulty()
