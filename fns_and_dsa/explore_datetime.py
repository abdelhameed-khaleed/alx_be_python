from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", current_date)


display_current_datetime()
nm_days = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date(nm_days):
    future_date = datetime.now() + timedelta(days=nm_days)
    print("Future date:", future_datestrftime("%Y-%m-%d"))


calculate_future_date(nm_days)
