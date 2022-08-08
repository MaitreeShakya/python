from ceasar_cipher_helper import alphabet, alphabets
from FunctionsWithInputs import greet
from art import logo

print(logo)
greet("Ceaser Cipher")


# Combining encrpyt and decrypt functions
def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for n in start_text:
        if n not in alphabets:
            end_text += n
        else:
            position = alphabets.index(n)
            new_position = position + shift_amount
            end_text += alphabets[new_position]

    print(f"The {cipher_direction}d text is: {end_text}")


def ask_again():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(text, shift, direction)


should_continue = True

while should_continue:
    ask_again()
    result = input("Do you want to run again? ").lower()
    if result == "no":
        should_continue = False
        print("Thank you for using Ceaser Cipher. Goodbye.")
