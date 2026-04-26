import random
import string

print("Password generator")

length = int(input("Enter password length:" ))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols

password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Generated password:", password)
