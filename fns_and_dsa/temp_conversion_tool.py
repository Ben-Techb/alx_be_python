FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main():
    try:
        temperature_input = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'fahrenheit':
            converted_temp = convert_to_celsius(temperature_input)
            print(f"{temperature_input}° Fahrenheit is equal to {converted_temp:.2f}° Celsius.")
        elif unit == 'celsius':
            converted_temp = convert_to_fahrenheit(temperature_input)
            print(f"{temperature_input}° Celsius is equal to {converted_temp:.2f}° Fahrenheit.")
        else:
            print("Invalid unit. Please enter either 'Celsius' or 'Fahrenheit'.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

