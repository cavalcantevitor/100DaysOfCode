# Basic Calculator
import art

# Printing logo
print(art.logo)

# Addition
def add(n1, n2):
    """Sum the numbers n1 and n2"""
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    """Subtract the numbers n1 and n2"""
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    """Multiply the numbers n1 and n2"""
    return n1 * n2


# Division
def divide(n1, n2):
    """Divide the numbers n1 and n2"""
    return n1 / n2


# Operations Dictionary

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    continue_calculating = True
    num = float(input("What's the first number? "))
    for key in operations:
        print(key)

    while continue_calculating == True:
        operation = input("Pick another operation: ")
        new_num = float(input("What's the next number? "))
        calculation = operations[operation]
        result = calculation(num, new_num)

        print(f"{num} {operation} {new_num} = {result}")

        user_choice = input(
            f"Do you want to continue calculating with {result}? Type 'y' to continue or 'n' to start a new calculation: "
        )

        if user_choice == 'y':
            num = result
        else:
            continue_calculating = False
            calculator()


calculator()
