class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

def main():
    calculator = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Error: Please enter a valid integer choice.")
            continue

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break

        if choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    print("Result:", calculator.add(num1, num2))
                elif choice == 2:
                    print("Result:", calculator.subtract(num1, num2))
                elif choice == 3:
                    print("Result:", calculator.multiply(num1, num2))
                elif choice == 4:
                    print("Result:", calculator.divide(num1, num2))

            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
