def safe_divide(a, b):
    """
    Safely divide two numbers with error handling.
    """
    try:
        # Convert both inputs to floats
        num1 = float(a)
        num2 = float(b)

        # Check for division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero"

        return num1 / num2

    except ValueError:
        return "Error: Invalid input"
