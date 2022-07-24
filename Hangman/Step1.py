import random


print("\n***Welcome to the Hangman Start***\n")

word_list = ["ardvark", "baboon", "camel"]

# TO DO-1- Randomly choose word from the list

chosen_word = random.choice(word_list)

# TO DO-2- Ask user to guess a letter

guess = input("Guess a letter: ").lower()


# TO DO-3- Check if the letter is in the chosen word

for n in chosen_word:
    if n == guess:
        print("Right")
    else:
        print("Wrong")
