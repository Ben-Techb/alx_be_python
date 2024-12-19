num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Perform the calculation using a Match Case statement
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Error: Invalid operation selected.")
