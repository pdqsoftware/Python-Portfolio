import re

PATTERN = r"^[+\-*/]$"
PATTERN_LIST = "+, -, *, /"

#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

# TODO: Move the operation functions to their own library

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("=== Python CLI Simple Calculator ===")
    print(f"Available Operations: {PATTERN_LIST}")

    try:
        num1 = float(input("Enter first number: "))

        while True:
            op = input(f"Enter operation ({PATTERN_LIST}): ").strip()
            # Check validity of input
            if not bool(re.match(PATTERN, op)):
                print("Invalid entry - try again!")
                continue
            break

        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers.")

#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

if __name__ == "__main__":
    calculator()
