from datetime import datetime
from time import sleep


def display_current_datetime():
    # current_date = datetime.date()
    current_time = datetime.now().time().strftime("%H:%M:%S")
    current_date = datetime.now().date()
    # print(f"Current Date and Time : {current_date},{current_time}")
    nm_days = input("Enter a number of days")


display_current_datetime()
