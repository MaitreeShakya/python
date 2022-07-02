print("\n***Welcome to Mominos Pizza***\n")

size = input("What size pizza do you want? S, M or L ").upper()
add_pepperoni = input("Would you like pepperoni in your pizza? Y or N ").upper()
extra_cheese = input("Would you like extra cheese in your pizza? Y or N ").upper()
total_bill = 0

if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
else:
    total_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is ${total_bill}")
