FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit):
    return float(fahrenheit) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR


while True:
    temperature = input("Enter the temperature to convert: ")
    try:
        temperature = float(temperature)
        break
    except ValueError:
        print("Please enter a valid number for temperature.")

while True:
    type = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").lower().strip()
    if type in ('c', 'f'):
        break
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if type == 'c':
    print(f"{convert_to_fahrenheit(temperature)} F")
elif type == 'f':
    print(f"{convert_to_celsius(temperature)} C")
