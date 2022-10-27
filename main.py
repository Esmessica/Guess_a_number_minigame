import random
from welcome__text import WelcomeText
from option_texts import OptionTexts
from Guess_number import Range

top_of_range = Range()
option = OptionTexts()
welcome_text = WelcomeText()

on = True
while on:
    print(welcome_text)
    top_of_range.top_range()
    limit = top_of_range.limit()
    random_number = random.randrange(0, limit)
    guesses = 0

    while on:
        guesses = guesses + 1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)

        else:
            print(option.wrong_type)
            continue

        if user_guess == random_number:
            print(option._coment_1)
            on = False
        elif user_guess > random_number:
            print("You were above the number.")
        else:
            print("You were below the number!")

print("\n\nYou got it in", guesses, "guesses!\n")
input()