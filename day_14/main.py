from art import logo, vs
from game_data import data
from random import choice

print(logo)
score = 0
is_game_over = False
account_b = choice(data)


def format_account_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def print_versus_info(first_account, second_account):
    print(f"Compare A: {format_account_data(first_account)}")
    print(vs)
    print(f"Against B: {format_account_data(second_account)}")


def check_answer(user_guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


while not is_game_over:
    # To preserve previous account at position B
    account_a = account_b
    account_b = choice(data)

    while account_a == account_b:
        account_b = choice(data)

    print_versus_info(account_a, account_b)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True

    # Make the game repeatable

    # making account at position B become to A
