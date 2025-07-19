import time
Monthly_income = input("Enter your monthly income : ")
Monthly_expenses = input("Enter your total monthly expenses:")

monthly_savings = float(Monthly_income) - float(Monthly_expenses)

print("Your monthly savings are: ", monthly_savings)

time.sleep(2)

print(
    f"Projected savings after one year, with interest {.05} is: {monthly_savings * 12}")
