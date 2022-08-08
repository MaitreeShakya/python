from ceasar_cipher_helper import alphabet, alphabets

# Angela Style
def encryptUdemStyle(plain_text, shift_amount):
    cipher_text = ""
    for n in plain_text:
        position = alphabet.index(n)
        newPosition = position + shift_amount
        cipher_text += alphabets[newPosition]
    print(f"The encrypted value is {cipher_text} UdemStyle.")


# My Encryption Style
def encrypt(plain_text, shift_amount):
    alphabet_length = len(alphabet)
    cipher_text = ""
    for n in plain_text:
        for a in range(0, len(alphabet)):
            if alphabet[a] == n:
                shifted_index = a + shift_amount
                if shifted_index > alphabet_length:
                    shift_diff = shifted_index - alphabet_length
                    cipher_text += alphabet[shift_diff]
                else:
                    cipher_text += alphabet[shifted_index]

    print(f"The encrypted text is: {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for n in cipher_text:
        for a in range(0, len(alphabet)):
            if alphabet[a] == n:
                plain_text += alphabet[a - shift_amount]
    print(f"The decrypted text is: {plain_text}")
