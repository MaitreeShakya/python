import random

print("\n***WELCOME to the PyPassword Generator***\n")

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

num_of_letters = int(input("How many letters would you like in your password? \n"))
num_of_symbols = int(input("How many symbols would you like in your password? \n"))
num_of_numbers = int(input("How many numbers would you like in your password? \n"))

random_letters = ""
random_symbols = ""
random_numbers = ""

for n in range(1, num_of_letters + 1):
    random_letters += random.choice(letters)
for n in range(1, num_of_symbols + 1):
    random_symbols += random.choice(symbols)
for n in range(1, num_of_numbers + 1):
    random_numbers += random.choice(numbers)

total_char = random_letters + random_numbers + random_symbols
total_char_len = len(total_char)

char_list = []

shuffled_char = ""


for n in range(0, total_char_len):
    char_list += total_char[n]


random.shuffle(char_list)


for n in range(1, len(char_list)):
    shuffled_char += char_list[n]

print(f"Your easy password is {total_char}\n")
print(f"Your hard password is {shuffled_char}")
