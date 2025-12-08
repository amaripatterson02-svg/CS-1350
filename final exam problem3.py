def safe_calculate(num1, num2, operation):
    """
    Perform arithmetic operation with exception handling.
    """

    try:
        # Step 1: Convert inputs to numbers
        num1 = float(num1)
        num2 = float(num2)

        # Step 2: Check if operation is valid
        if operation not in ['+', '-', '*', '/']:
            return "Error: Invalid operation"

        # Step 3 & 4: Perform the operation
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2

    except ValueError:
        # Step 5: Handle invalid number conversion
        return "Error: Invalid number"
    except ZeroDivisionError:
        # Extra safety (though already handled above)
        return "Error: Division by zero"
