import random

print("\n***Welcome to the Banker Roulette***\n")

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

# random_choice = random.randint(0, len(names) - 1)
# print(random_choice)

print(f"\n{random.choice(names)} is going to buy the lunch. ")
