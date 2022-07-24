import random

print("\n***Welcome to the Hangman Step 3***\n")



word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
display = []
count = 0
end_of_game = False

for n in chosen_word:
    display += "_"


# ToDo 1: Loop through until the game is won

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for n in range(0, chosen_word_length):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = guess
    print(f"\n{display}\n")
    if "_" not in display:
        end_of_game = True
