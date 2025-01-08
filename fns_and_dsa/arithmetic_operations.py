def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation based on the input parameters.
    
    :param num1: First number (float)
    :param num2: Second number (float)
    :param operation: Operation to perform (string: 'add', 'subtract', 'multiply', or 'divide')
    :return: Result of the operation or an appropriate error message
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

