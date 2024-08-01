def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Example usage:
celsius = 25
fahrenheit = 77
kelvin = 298.15

print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
print(f"{celsius}°C is {celsius_to_kelvin(celsius)}K")
print(f"{kelvin}K is {kelvin_to_celsius(kelvin)}°C")
print(f"{fahrenheit}°F is {fahrenheit_to_kelvin(fahrenheit)}K")
print(f"{kelvin}K is {kelvin_to_fahrenheit(kelvin)}°F")
