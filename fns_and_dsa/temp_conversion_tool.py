global FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
global CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit):
    return float(fahrenheit) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR


temperature = input("Enter the temperature to convert: ")

type = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): ").lower().strip()

if type == 'c':
    print(f"{convert_to_fahrenheit(temperature)} F")
elif type == 'f':
    print(f"{convert_to_celsius(temperature)} C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# what is input validations ?
