# Basic Calculator Program
# Get user input for two numbers - also added error handling for non-numeric input
running = input("Would you like to use the calculator? (yes/no): ")
if running =="yes":
    running = True
else:
    running = False
while running == True:
    try:
        value1 = float(input("Enter first number: "))
        value2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        exit()
# Ask the user to choose an operation    
    operation = input("Enter operation (+, -, *, /): ")
# Perform the calculation based on the chosen operation
    if operation == '+':
        result = value1 + value2
    elif operation == '-':
        result = value1 - value2
    elif operation == '*':
        result = value1 * value2
    elif operation == '/':
        if value2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = value1 / value2
    else: 
        result = "You have not seleceted a valid operation, please try again."
        
    result = round(result, 2)
    print(f"The result is: {result}")
    running = input("Would you like to perform another calculation? (yes/no): ")
    if running =="yes":
        running = True
    else:
        running = False
print("Thank you for using the calculator. Goodbye!")