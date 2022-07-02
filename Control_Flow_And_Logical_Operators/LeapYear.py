print("***Welcome to the Leap year challenge***\n")

year_to_check = int(input("Which year do you want to check? "))

divisible_by_4 = year_to_check % 4 == 0
divisible_by_100 = year_to_check % 100 == 0
divisible_by_400 = year_to_check % 400 == 0


if divisible_by_4:
    if divisible_by_100:
        if divisible_by_400:
            print(f"The year {year_to_check} is a leap year.")
        else:
            print(f"The year {year_to_check} is not a leap year.")
    else:
        print(f"The year {year_to_check} is a leap year.")
else:
    print(f"The year {year_to_check} is not a leap year.")
