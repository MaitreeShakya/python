import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0


def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS
    return turns


def check_answer(guess_number, answer, turns):
    if guess_number > answer:
        print("Too High")
        return turns - 1
    elif guess_number < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {guess_number}")


def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    continue_playing = True
    turns = set_difficulty()

    while continue_playing:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guessess, you lose.")
            continue_playing = False
        elif guess != answer:
            print("Guess again.")


game()
