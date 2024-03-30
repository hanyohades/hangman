from words_db import EASY_WORDS, MEDIUM_WORDS, HARD_WORDS
from random import randint
import os
from chromaconsole import Color, Style
from model import my_model

RED = '#FF0000'
GREEN = '#00FF00'
YELLOW = '#FFFF00'


def select_level() -> str:
    print("Choose your word level:")
    print("  1. Easy")
    print("  2. Medium")
    print("  3. Hard")
    level = input("> ")
    if level == '1' or level.lower() == 'easy':
        return EASY_WORDS
    elif level == '2' or level.lower() == 'medium':
        return MEDIUM_WORDS
    elif level == '3' or level.lower() == 'hard':
        return HARD_WORDS

def validate_input(player_guess, guess_holder):
    if not player_guess.isalpha():
        print(f"{Color.text(RED)}Please in put a letter!{Style.reset()}\n")
        return False
    elif len(player_guess) > 1:
        print(f"{Color.text(RED)}Only one letter allowed!{Style.reset()}\n")
        return False
    elif player_guess in guess_holder:
        os.system('clear')
        print(f"{Color.text(RED)}You have already guessed that letter!\n")
        print(f"The letters you already guessed:  {guess_holder}{Style.reset()}")
        return False
    return True


def show_word(word, guess_holder):
    output = []
    for letter in word:
        output.append('_' if letter not in guess_holder else letter.upper())
    print(f"{Color.text(GREEN)}{output}{Style.reset()}\n")


def mainloop():
    db = select_level()
    word = db[randint(0, len(db)-1)]
    guess_holder = []
    revealed_count = 0
    player_guess = None
    user_health = len(my_model) - 1

    while True:
        print(my_model[user_health])
        print(f"{Color.text(YELLOW)}Your still have {user_health} guesses{Style.reset()}\n")
        show_word(word, guess_holder)

        player_guess = str(input("Take a guess: ")).lower()
        if not validate_input(player_guess, guess_holder):
            continue

        guess_holder.append(player_guess)
        if player_guess not in word:
            user_health -= 1

        else:
            revealed_count += word.count(player_guess)

        if revealed_count == len(word):
            print(f"\n{Color.text(GREEN)}Congratulation! The word is: {word.upper()}{Style.reset()}\n")
            break


        if user_health == 0:
            print(f"{Color.text(RED)}You ran out of guesses... The word is: {word.upper()}{Style.reset()}")
            break

        os.system('clear')

if __name__ == '__main__':
    try:
        mainloop()
    except KeyboardInterrupt:
        print("\nGood Bye!")
