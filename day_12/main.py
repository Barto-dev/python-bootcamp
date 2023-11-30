from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def print_game_info():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def print_guess_result(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}")
    elif guess < answer:
        print("Too low")
    else:
        print("Too high")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def change_turns(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess < answer:
        return turns - 1
    elif guess > answer:
        return turns - 1


def game():
    print_game_info()

    answer = randint(1, 100)
    game_over = False
    turns = set_difficulty()

    while not game_over:
        guess = int(input("Make a guess: "))
        print_guess_result(guess, answer)
        turns = change_turns(guess, answer, turns)

        if guess == answer:
            game_over = True
        elif turns == 0:
            print(f"You've run out of guesses, you lose. The answer was {answer}")
            game_over = True
        else:
            print(f"You have {turns} remaining to guess number")


game()
