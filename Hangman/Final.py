import os
import random
from hangman_words import word_list
from hangman_art import logo, stages

print("\n***Welcome to the Hangman***\n")
print(logo)

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
display = []
lives = 6
end_of_game = False


def clear():
    os.system("cls")


for n in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You have already guessed {guess}")
    else:
        for n in range(0, chosen_word_length):
            letter = chosen_word[n]
            if letter == guess:
                display[n] = guess

        if guess not in chosen_word:
            print(stages[lives])
            print(f"You guessed {guess}, that's not in the word. You lost a life. You have {lives} left")
            lives -= 1
            if lives < 0:
                end_of_game = True
                print(f"\nYou lost. The word is {chosen_word}\n")

        if "_" not in display:
            end_of_game = True
            print(f"\n{' '.join(display)}")
            print("\nYou Win.\n")

        if not end_of_game:
            print(f"\n{' '.join(display)}\n")
