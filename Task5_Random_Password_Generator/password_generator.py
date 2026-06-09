import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

length = int(input("Enter the desired password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)

print("\nThank you for using the Random Password Generator!")
