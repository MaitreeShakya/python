import random

print("\n***Welcome to the Hangman Step 3***\n")

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
display = []
lives = 6
end_of_game = False

for n in chosen_word:
    display += "_"


# ToDo 1: Keep Track of Lives

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for n in range(0, chosen_word_length):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = guess

    if guess not in chosen_word:
        print(stages[lives])
        lives -= 1
        if lives < 0:
            end_of_game = True
            print("You lost.")

    if "_" not in display:
        end_of_game = True
        print("\nYou Win.\n")
    else:
        print(f"\n{' '.join(display)}\n")
