def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2

import art
print(art.logo)
operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide

}


def calculator():
    continue_calculation = True

    n1 = float(input("What is the first number: "))

    while continue_calculation:
        for symbol in operations:
            print(symbol)

        operation_chose = input("Pick an operation: ")
        n2 = float(input("What is the second number: "))

        calculation_function = operations[operation_chose]
        result = calculation_function(n1, n2)
        print(f"{n1} {operation_chose} {n2} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
        if cont == 'y':
            n1 = result  # Continue with the result as the first number
        else:
            continue_calculation = False
            calculator()  # Start a new calculation


calculator()