import random


print("\n***Welcome to the Rock, Paper and Scissors Game.***\n")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

options = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number.")
else:
    print(f"You chose: {options[player_choice]}\nComputer chose: {options[computer_choice]}")

    if player_choice == 0 and computer_choice == 2:
        print("You Win")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose")
    elif player_choice > computer_choice:
        print("You Win.")
    elif player_choice < computer_choice:
        print("You Lose.")
    elif player_choice == computer_choice:
        print("Its a draw")
