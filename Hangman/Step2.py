import random

print("\n***Welcome to the Hangman Step 2***\n")

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)

# TO DO - 1: Create empty list for chosen word and replace letters with "_"
display = []

for n in chosen_word:
    display.append("_")

# TO DO - 2: Ask user to guess and if its a match replace empty letter with guessed letter


guess = input("Guess a letter: ").lower()

for n in range(0, chosen_word_length):
    if chosen_word[n] == guess:
        display[n] = guess

print(f"\n{display}\n")
