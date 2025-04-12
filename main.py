# Higher or Lower Game

import random
from art import logo, vs
from game_data import data

# Score tracking
score = 0

# Function to get random account from data
def get_random_account():
    return random.choice(data)

# Function to format account for display
def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to compare followers
def is_correct_guess(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
account_a = get_random_account()
account_b = get_random_account()

# Make sure account_a and account_b are not the same
while account_a == account_b:
    account_b = get_random_account()

game_should_continue = True

while game_should_continue:
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = is_correct_guess(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"\nYou got it right! Current score: {score}.\n")
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()
    else:
        game_should_continue = False
        print(f"\nSorry, that's wrong. Final score: {score}")
