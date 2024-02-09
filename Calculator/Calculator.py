def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {"+": add, "-": subtract, "/": divide, "*": multiply}

from art import logo


def calculator():
    should_continue = True
    print(logo)
    n1 = float(input("Welcome to calculator!\nInput the first number\n"))
    for symbols in operators:
        print(symbols)
    while should_continue:
        given_operators = input("Pick the operator\n")
        n2 = float(input("Input the next number\n"))
        calculation_function = operators[given_operators]
        first_answer = calculation_function(n1, n2)
        print(f"{n1} {given_operators} {n2} = {first_answer}")
        restart = input(f"Type y to calculate with {first_answer}, type n to restart\n")
        if restart == "y":
            n1 = first_answer
        else:
            should_continue = False
            calculator()


calculator()
