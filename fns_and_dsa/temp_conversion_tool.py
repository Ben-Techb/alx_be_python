FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor from Celsius to Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main function to interact with the user
def main():
    try:
        temperature_input = float(input("Enter the temperature: "))
        unit = input("Is the temperature in Celsius or Fahrenheit? ").strip().lower()

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

