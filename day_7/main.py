import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
end_of_game = False
lives = 6


def print_failure_info(input_letter):
    print(f"You guessed '{input_letter}', that's not in the word.")
    print('---------------')
    print(stages[lives])


print(logo)

for i in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
        print_failure_info(guess)
        if lives == 0:
            end_of_game = True
            print("You lose")
    else:
        if guess in display:
            print(f"You've already guessed '{guess}'")
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = letter
        print(f"{' '.join(display)}")

    guess_word = "".join(display)
    if guess_word == chosen_word:
        end_of_game = True
        print("You won")
