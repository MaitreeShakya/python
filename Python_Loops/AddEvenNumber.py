print("\n***WELCOME TO THE ADD EVEN NUMBER***\n")


total_even = 0
total_even2 = 0
for num in range(2, 101, 2):
    total_even += num

for num in range(1, 101):
    if num % 2 == 0:
        total_even2 += num

print(f"The total is {total_even} {total_even2}")
