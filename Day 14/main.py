import random
from art import logo
from game_data import data

print(logo)

def random_account():
    """return random account"""
    return random.choice(data)

def format_data(account):
    """Format the account data into a printable string."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def check_answer (guess, follower_a, follower_b):
    if follower_a>follower_b:
        return guess== "a"
    else:
        return guess=="b"


def play_game():
    print("Welcome to the Instagram follower guessing game!")

    score = 0
    game_over = False
    account_a = random_account()

    while not game_over:
        account_b = random_account()
        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {format_data(account_a)}")
        print("VS")
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)
        print(logo)
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = account_b  # The winner becomes the next 'A'
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()