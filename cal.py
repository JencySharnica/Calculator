def calculator():
    print("Operations: add, sub, multiply, divide")
    operation = input("Enter operation: ")

    if operation not in ["add", "sub", "multiply", "divide"]:
        print("Error: Invalid operation.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Error: Unknown operation.")
        return

    print("Result:", result)


calculator()