def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        return f"The result of the division is {num / denom}"
    except ValueError:
        print(" Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print(" Error: Please enter numeric values only.")
