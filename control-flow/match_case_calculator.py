num1 = 0
num2 = 0


num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
result = 0

match (operation):
    case "-":
        result = float(num1) - float(num2)
    case "*":
        result = float(num1) * float(num2)
    case "/":
        if float(num2) != 0:
            result = float(num1) / float(num2)
        else:
            result = "Error: Division by zero is not allowed."
    case "+":
        result = float(num1) + float(num2)
    case _:
        print("Invalid operation selected.")

print(f"The result is: {result}")
