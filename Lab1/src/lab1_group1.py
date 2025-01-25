############################################################################
# Program:      Secure Password Generator
# Authors:      Jayce Baxter and Oryon Facey
# Date:         January 24th, 2025
# Description:  Generates a secure password with a user-defined number of
#               letters, numbers, and symbols
############################################################################


import random
import string

# Initializing variables
password_length_valid = False
num_of_letters = 0
num_of_digits = 0
num_of_symbols = 0
min_value = 0
password_length = 0
max_value = password_length

# Initializing lists
password = []

# Functions
# this asks the user for their input for the letters, digits and special characters
def get_user_input(min_value, max_value):
    prompt = "Please enter a integer value between " + str(min_value) + " and " + str(max_value)
    input_conditions_met = False
    new_input = 0
    while not input_conditions_met:
        try:
            new_input = int(input(prompt + " "))
        except:
            print("Please enter a number a positive whole number")
        if  new_input > max_value:
            print("Please enter a positive whole number less than " + str(max_value))
            continue
        elif new_input < min_value:
            print("Please enter a positive whole number more than " + str(min_value))
            continue
        else:
            max_value = max_value - new_input
            input_conditions_met = True
    return max_value, new_input
# This creates the randomization of the users password
def create_password(num_of_letters, num_of_digits, num_of_symbols, password_length):
    length_of_password = 0
    letter_count = 0
    digit_count = 0
    symbol_count =0
    while length_of_password < password_length:
        if letter_count < num_of_letters and digit_count < num_of_digits and symbol_count < num_of_symbols:
            option = random.randint(1, 3)
            if option == 1:
                password.append(random.choice(string.ascii_letters))
                letter_count = letter_count + 1
            elif option == 2:
                password.append(random.choice(string.digits))
                digit_count = digit_count + 1
            else:
                password.append(random.choice(string.punctuation))
                symbol_count = symbol_count + 1
        elif letter_count < num_of_letters and digit_count < num_of_digits and symbol_count == num_of_symbols:
            option = random.randint(1, 2)
            if option == 1:
                password.append(random.choice(string.ascii_letters))
                letter_count = letter_count + 1
            else:
                password.append(random.choice(string.digits))
                digit_count = digit_count + 1
        elif digit_count < num_of_digits and symbol_count < num_of_symbols and letter_count == num_of_letters:
            option = random.randint(1, 2)
            if option == 1:
                password.append(random.choice(string.digits))
                digit_count = digit_count + 1
            else:
                password.append(random.choice(string.punctuation))
                symbol_count = symbol_count + 1
        elif symbol_count < num_of_symbols and letter_count < num_of_letters and digit_count < num_of_digits:
            option = random.randint(1, 2)
            if option == 1:
                password.append(random.choice(string.punctuation))
                symbol_count = symbol_count + 1
            else:
                password.append(random.choice(string.ascii_letters))
                letter_count = letter_count + 1
        elif letter_count < num_of_letters and digit_count == num_of_digits and symbol_count == num_of_symbols:
            password.append(random.choice(string.ascii_letters))
        elif digit_count < num_of_digits and letter_count == num_of_letters and symbol_count == num_of_symbols:
            password.append(random.choice(string.digits))
        else:
            password.append(random.choice(string.punctuation))
        length_of_password = length_of_password + 1
    return password




# The start of our program
if __name__ == "__main__":
    while not password_length_valid:
        try:
            password_length = int(input("Please enter the desired length of the password, must be a positive whole number: "))
        except:
            print("Please enter a positive whole number")
            continue
        if password_length <= min_value:
            print("Please enter a positive whole number")
            continue
        else:
            password_length_valid = True
    max_value = password_length

    print("Enter the number of letters you would like to use.")
    max_value, num_of_letters = get_user_input(min_value, max_value)

    print("Enter the number of digits you would like to use.")
    max_value, num_of_digits = get_user_input(min_value, max_value)

    # to make sure we use all the password length
    print("Enter the number of special character you would like to use.")
    min_value = max_value
    max_value, num_of_symbols = get_user_input(min_value, max_value)

    password = create_password(num_of_letters, num_of_digits, num_of_symbols, password_length)
    user_password = "".join(str(x) for x in password)

    print(user_password)