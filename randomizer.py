"""
Password Manager Password Randomizer
Author(s): Carlos Navarro-Montanez
Date: November 11th, 2025
"""
def generate_password():
    import random
    upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_amt = 0
    lower_char = "abcdefghijklmnopqrstuvwxyz"
    lower_amt = 0
    digits = "0123456789"
    digits_amt = 0
    special_char = ""
    special_amt = 0

    print("Welcome to the Password Randomizer!")
    print("This tool will help you generate a strong password.")
    print("Please type the special characters you want to include in your password (e.g., !@#$%^&*):")
    special_char = input("Special Characters: ")
    length = int(input("Total Password Length: "))
    upper_amt = int(input("Number of Uppercase Letters: "))
    lower_amt = int(input("Number of Lowercase Letters: "))
    digits_amt = int(input("Number of Digits: "))
    special_amt = int(input("Number of Special Characters: "))

    #Empty list to hold password characters
    password_chars = []
    #Add required characters to the password list
    password_chars += random.choices(upper_char, k=upper_amt)
    password_chars += random.choices(lower_char, k=lower_amt)
    password_chars += random.choices(digits, k=digits_amt)
    password_chars += random.choices(special_char, k=special_amt)

    #Validate total length
    if len(password_chars) > length:
        raise ValueError("The sum of specified character amounts exceeds the total password length.")
    elif len(password_chars) < length:
        raise ValueError("Specified requirements do not fill the total length.")
    
    #Shuffle the characters to ensure randomness
    random.shuffle(password_chars)
    generated_pass = ''.join(password_chars)
    return generated_pass

print("Generating password...")
print("Your generated password is:")
print(generate_password())