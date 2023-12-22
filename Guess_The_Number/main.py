


# #Number Guessing Game Objectives:

# # Include an ASCII art logo.
# # Allow the player to submit a guess for a number between 1 and 100.
# # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# # If they got the answer correct, show the actual answer to the player.
# # Track the number of turns remaining.
# # If they run out of turns, provide feedback to the player. 
# # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    

def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print('Too high.')
        return turns - 1
    elif guess < answer:
        print('Too low.')
        return turns - 1
    else:
        print(f'you got it! The answer was {answer}.')

def game():
    turns = 0
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        guess = int(input('Make a guess: '))
        print(f'You have {turns} attempts remaining to guess the number.')
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('You have run out of guesses, you lose.')
            return
        elif guess != answer:
            print('Guess again.')






# import random

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# number = random.randint(1, 100)
# attempts = 0
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# if difficulty == "easy":
#     attempts = 10
# else:
#     attempts = 5

# def play_game(numOfAttempts):
#     for i in range(numOfAttempts):
#         print(f"You have {numOfAttempts} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         if guess == number:
#             print(f"You got it! The answer was {number}.")
#             play_again = input("Do you want to play again? Type 'y' or 'n': ")
#             if play_again == "y":
#                 play_game()
#             else:
#                 print("Goodbye.")
#             break
#         elif guess > number:
#             print("Too high.")
#             numberOfAttempts -= 1
#         else:
#             print("Too low.")
#             numberOfAttempts -= 1


# play_game(attempts)



