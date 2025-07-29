def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
    except ValueError as e:
        print(" Error: Please enter numeric values only.")
    else:
        return num / denom
