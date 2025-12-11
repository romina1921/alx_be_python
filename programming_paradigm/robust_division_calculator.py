def safe_divide(numerator, denominator):
    """
    Perform division safely, handling non-numeric input and division by zero.

    Args:
        numerator: The numerator (str or number)
        denominator: The denominator (str or number)

    Returns:
        str: Result of division or an error message
    """
    # Attempt to convert inputs to floats
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Handle division by zero
    try:
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
