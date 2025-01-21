import random
import string

# Initializing variables
validation = False

# Initializing lists
letters = []
digits = []
symbols = []

# Generate a random special character
random_special = random.choice(string.punctuation)

while validation == False:

    # Prompts the user for password length
    password_length = input("Please enter the desired length of the password.")

    # Prompts the user for number of letters
    no_of_letters = input("Please enter the number of letters")

    for i in no_of_letters:
        # Generate a random letter
        random_letter = random.choice(string.ascii_letters)
        letters.append(random_letter)

    # Prompts the user for number of digits
    no_of_digits = input("Please enter the number of digits")

    for i in no_of_digits:
        # Generate a random digit
        random_digit = random.choice(string.digits)
        digits.append(random_digit)

# Prompts the user for number of symbols
no_of_symbols = input("Please enter the number of symbols")

try:
    no_of_letters = int(no_of_letters)
    no_of_digits = int(no_of_digits)
    no_of_symbols = int(no_of_symbols)

except: