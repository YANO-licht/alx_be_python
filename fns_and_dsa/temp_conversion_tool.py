FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    x = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"The temperature in celcius is {x}")
    return x

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    x = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"The temperature in fahrenheit is {x}")
    return x

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

temperature = input("Enter the temperature to convert: ")
if is_number(temperature):
    temperature = float(temperature)

    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if temperature_type == 'F':
        convert_to_celsius(temperature)
    elif temperature_type == 'C':
        convert_to_fahrenheit(temperature)
    else:
        print("Please enter valid option")
else:
    print("Invalid temperature. Please enter a numeric value.")