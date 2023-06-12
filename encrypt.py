import random
import string

def generate_key():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return {char: i+1 for i, char in enumerate(alphabet)}

def encrypt(message, key):
    encrypted = []
    for i, char in enumerate(message):
        n = key[char]
        if i == 0:
            encrypted.append(n)
        else:
            encrypted.append((encrypted[-1] * n) % 26)
    return encrypted

def decrypt(encrypted, key):
    reversed_key = {v: k for k, v in key.items()}
    message = []
    for i, num in enumerate(encrypted):
        if i == 0:
            message.append(reversed_key[num])
        else:
            message.append(reversed_key[(num * pow(encrypted[i-1], -1, 26)) % 26])
    return ''.join(message)

key = generate_key()

message = 'hello'
encrypted = encrypt(message, key)
print('Encrypted:', encrypted)

decrypted = decrypt(encrypted, key)
print('Decrypted:', decrypted)


  # Randomize the alphabet.
    #Assign each letter of the alphabet a number from 1 to 26.
    #For each letter in the input message:
    #Convert the letter to its corresponding number n.
    #Multiply the previous encrypted number by n, and then take the result modulo 26.
        #If the result is 0, replace it with 26 (to keep the range between 1 and 26).
