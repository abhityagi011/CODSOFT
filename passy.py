import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for password length
try:
    user_length = int(input("Enter the desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
7