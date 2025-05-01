#Password Randomizer in Python by Carlos Navarro-Montanez

#Import the random library
import random

#Obtain the user's password requirements
#Password length
pass_length = int(input("What is the desired length of the password? "))

#Obtain the eligibile symbols for the password if the symbols amount is greater than 0
sym_str = input("What are the eligibile symbols (input them one by one with no spaces)? ")
sym_list = []
for symbol in sym_str:
        sym_list.append(symbol)

#Check if the user wants a requirement fulfilling password and prompt the user if the answer is 'Y' (yes)
pass_type = input('Type capital "Y" if you want a requirement fulfilling password: ')
if pass_type == 'Y':
    #Password numbers
    num_amount = int(input("What is the minimum amount of numbers the password should have? "))
    #Password upppercase letters    
    up_amount = int(input("What is the minimum amount of uppercase letters the password should have? "))
    #Password lowercase letters
    low_amount = int(input("What is the minimum amount of lowercase letters the password should have? "))
    #Password symbols amount
    sym_amount = int(input("What is the minimum amount of symbols the password should have? "))
    #Check if the requirements for the idexes of the password are greater than the minimum password length specified by the user
    user_total = num_amount + up_amount + low_amount + sym_amount
    if user_total != pass_length:
        print('The user requirements for the specifics of the password are not equal to the desired length specified.')
        print('Try Again.')
        quit()

#Initialize string of uppercase letters
up_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Change the uppercase string into an uppercase list
up_list = []
for up_letter in up_str:
    up_list.append(up_letter)
    

#Initialze string of lowercase letters
low_str = 'abcdefghijklmnopqrstuvwxyz'

#Change the lowercase string into a lowercase list
low_list = []
for low_letter in low_str:
    low_list.append(low_letter)

#Requirements fufilling password generation function
def specified_pass(num_amt, up_amt, low_amt, sym_amt,up_lst, low_lst, sym_lst):
    password = ''
    for i in range(num_amt):
        current_num = str(random.randint(0,9))
        password += current_num
    for j in range(up_amt):
        current_up = random.choice(up_lst)
        password += current_up
    for k in range(low_amt):
        current_low = random.choice(low_lst)
        password += current_low
    for m in range(sym_amt):
        current_sym = random.choice(sym_lst)
        password += current_sym
    return(password)
    
#Completely random password generation function
def random_pass(pass_length, up_list, low_list, sym_list):
    options = ['num','up','low','sym']
    password = ''
    for i in range(pass_length):
        current_option = random.choice(options)
        if current_option == 'num':
            current_num = str(random.randint(0,9))
            password += current_num
        if current_option == 'up':
            current_up = random.choice(up_list)
            password += current_up
        if current_option == 'low':
            current_low = random.choice(low_list)
            password += current_low
        if current_option == 'sym':
            current_sym = random.choice(sym_list)
            password += current_sym
    return(password)

#Generate the password based on the users' password preference
if pass_type == 'Y':
    print(specified_pass(num_amount, up_amount, low_amount, sym_amount, up_list, low_list, sym_list))
else:
    print(random_pass(pass_length, up_list, low_list, sym_list))