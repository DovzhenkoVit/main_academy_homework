def calculator():
    a = int(input("Enter first number: "))
    c = input("Enter the operation(+, -, /, *): ")
    b = int(input("Enter second number: "))

    if c == "+":
        add = a + b
        print(add)

    elif c == "-":
        subtraction = a - b
        print(subtraction)

    elif c == "*":
        multiplication = a * b
        print(multiplication)

    elif c == "/":
        if b != 0:
            division = a / b
            print(division)

        print("Division by zero!")

    else:
        print("Error!")


if __name__ == '__main__':
    calculator()
