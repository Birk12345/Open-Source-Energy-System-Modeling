import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers, handling division by zero
def divide(x, y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

# Function to perform the selected operation based on user input
def calculate(choice, num1, num2):
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            return add(num1, num2)
        elif choice == '2':
            return subtract(num1, num2)
        elif choice == '3':
            return multiply(num1, num2)
        elif choice == '4':
            return divide(num1, num2)
    else:
        return "Invalid input"  # Return a message for invalid input

# Call the function to start the calculator
if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Enter choice of operation
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = calculate(choice, num1, num2)
    print("Result:", result)
