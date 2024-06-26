import random
import string


def generate_password(min_length, numbers=True, special_charecters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    charecters = letters
    if numbers:
        charecters += digits
    if special_charecters:
        charecters += special

    pwd = ""
    meets_criteria = False 
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(charecters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_charecters:
            meets_criteria = meets_criteria and has_number

    return pwd


min_length = int(input("Enter the minimun length"))
has_number = input("do you want to include numbers(y/n)?").lower() == "y"
has_special = input("do you want to include special charecters(y/n)?").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password i:", pwd)


