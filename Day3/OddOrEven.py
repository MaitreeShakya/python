print("***Welcome to Odd or Even Challenge***\n")
number = int(input("Which number do you want to check? "))

isEven = number % 2 == 0

if isEven:
    print("This is an even number.")
else:
    print("This is an Odd number.")
