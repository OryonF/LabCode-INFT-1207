import random
import string

# Initializing variables
validation = False
password_length_valid = False
no_of_letters_valid = False
no_of_digits_valid = False
no_of_symbols_valid = False

# Initializing lists
letters = []
digits = []
symbols = []

# Generate a random special character
random_special = random.choice(string.punctuation)

while validation == False:

    # Prompts the user for password length and validates correct input
    while password_length_valid == False:

        password_length = input("Please enter the desired length of the password: ")

        try:
            password_length = int(password_length)
            password_length_valid = True

        except ValueError:
            print("Please enter a number")

    while no_of_letters_valid == False:

        no_of_letters = input("Please enter the number of letters: ")

        try:
            no_of_letters = int(no_of_letters)
            for i in range(no_of_letters):
                # Generate a random letter
                random_letter = random.choice(string.ascii_letters)
                letters.append(random_letter)
            no_of_letters_valid = True

        except ValueError:
            print("Please enter a number")


    while no_of_digits_valid == False:

        # Prompts the user for number of digits
        no_of_digits = input("Please enter the number of digits: ")

        try:
            no_of_digits = int(no_of_digits)
            for i in range(no_of_digits):
                # Generate a random digit
                random_digit = random.choice(string.digits)
                digits.append(random_digit)
            no_of_digits_valid = True

        except ValueError:
            print("Please enter a number")

    while no_of_symbols_valid == False:
        # Prompts the user for number of symbols
        no_of_symbols = input("Please enter the number of symbols: ")

        try:
            no_of_symbols = int(no_of_symbols)
            for i in range(no_of_symbols):
                # Generate a random special character
                random_special = random.choice(string.punctuation)
                symbols.append(random_special)
            no_of_symbols_valid = True

        except ValueError:
            print("Please enter a number")

    if password_length_valid == True and no_of_letters_valid == True \
        and no_of_digits_valid == True and no_of_symbols_valid == True:
        validation = True


print(letters, digits, symbols)
