print("\n***Welcome to the Love Calculator****\n")

your_name = input("Enter your name: ").lower()
crushes_name = input("Enter your crushes name: ").lower()

combined_name = your_name + crushes_name

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your love score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
