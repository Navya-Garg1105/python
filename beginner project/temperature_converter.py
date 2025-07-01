class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def fahrenheit_to_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(self, kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32

def main():
    converter = TemperatureConverter()

    while True:
        print("\n1. Celsius to Fahrenheit and Kelvin")
        print("2. Fahrenheit to Celsius and Kelvin")
        print("3. Kelvin to Celsius and Fahrenheit")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Goodbye!")
            break

        temp = float(input("Enter temperature: "))

        if choice == '1':
            print("Fahrenheit:", converter.celsius_to_fahrenheit(temp))
            print("Kelvin:", converter.celsius_to_kelvin(temp))
        elif choice == '2':
            print("Celsius:", converter.fahrenheit_to_celsius(temp))
            print("Kelvin:", converter.fahrenheit_to_kelvin(temp))
        elif choice == '3':
            print("Celsius:", converter.kelvin_to_celsius(temp))
            print("Fahrenheit:", converter.kelvin_to_fahrenheit(temp))
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
