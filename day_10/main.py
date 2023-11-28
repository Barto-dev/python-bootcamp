from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calc_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        operation = input("Pick operator, possible variants: '+', '-', '*', '/' ")
        num2 = float(input("What's the next number?: "))

        calculation_function = calc_operations[operation]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {float(result):g}")

        if input(f"Type 'y' to continue calculating with {float(result):g}, or type 'n' to start a new calculation: ") != 'y':
            should_continue = False
            calculator()
        else:
            num1 = result


calculator()
