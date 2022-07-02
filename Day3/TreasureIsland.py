print("\n***Welcome to Treasure Island***\n Your mission is to find the treasure.\n")
choice1 = input("You're at a cross road, Where do you want to go? Type \"left\" or \"right\". ")

if choice1.lower() == "left":
    choice2 = input(
        "\nYou came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim accross. "
    )

    if choice2.lower() == "wait":
        door = input(
            "\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? "
        )
        if door == "red":
            print("\nBurned by fire. Game Over.")
        elif door == "yellow":
            print("\nYou Win!")
        elif door == "blue":
            print("\nEaten by beasts. Game Over.")
        else:
            print("\nGame Over")
    else:
        print("\nAttacked by trout. Game Over.")
else:
    print("\nFall into a hole. Game Over.")
