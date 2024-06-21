alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + key) % 26
            result += alphabet[new_position]
        else:
            result += char
    print(f"The cipher text is: {result}")


def decrypt(cipher, key):
    plaintext = ""
    for char in cipher:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = (position - key) % 26
            plaintext += alphabet[new_pos]
        else:
            plaintext += char
    print(f"The plaintext is {plaintext}")


task = int(input("Enter 1 for encryption and 2 for decryption: "))
message = input("Enter Message: ")
shift = int(input("Enter shift key: "))
message = message.lower()
if task == 1:
    encrypt(plaintext=message, key=shift)

elif task == 2:
    decrypt(cipher=message, key=shift)
