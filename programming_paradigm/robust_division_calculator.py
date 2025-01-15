# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides the numerator by the denominator, handling common errors.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        str: A message with the result or an error explanation.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        # Perform division
        result = num / denom
        return f"The result is: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both inputs must be numeric."


