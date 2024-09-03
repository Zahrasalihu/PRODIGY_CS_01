letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if letter != " ":
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += letter  # Keep spaces as is

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if letter != " ":
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
        else:
            plaintext += letter  # Keep spaces as is

    return plaintext


print()
print("* CAESAR CIPHER TASK(PRODIGY INFOTECH) *")
print()

print("Would you like to encrypt or decrypt?")

user_input = input("encrypt/decrypt: ").lower()
print()

if user_input == "encrypt":
    print("ENCRYPTION MODE SELECTED")
    print()
    key = int(input("Enter the key between 1 and 26: "))
    text = input("Enter the text/data to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == "decrypt":
    print("DECRYPTION MODE SELECTED")
    print()
    key = int(input("Enter the key between 1 and 26) "))
    text = input("Enter the text/data to decrypt: ")
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')