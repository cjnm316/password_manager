#Four Function Calculator created by Carlos Navarro-Montanez
 
 #Print instructions
print("Simple Four Function Calculator created by Carlos Navarro-Montanez")
print("Use the +, -, *, and / symbols to make your computations")
print("Type 'QUIT' at the operation stage of any computation to quit the program at any point")
 
 #Filename to store computations
filename = input("What txt file do you want to write to or create? ")
file = open(filename, 'w')
 
 #Initialize variables input by the user
operation = input("Operation Symbol: ")
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
 
 #Loop to continue making computations until the user types quit
while operation != "QUIT":
    result = "N/A"
    computation = "N/A"
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("You can't divide a number by 0") 
    else:
        print("Invalid operation input")
    computation = f'{num1} {operation} {num2} = {result}\n'
    print(computation)
    file.write(computation)
    operation = input("Operation Symbol: ")
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

file.close()
         
