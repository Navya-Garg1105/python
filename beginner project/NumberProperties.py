class NumberProperties:
    def __init__(self, number):
        self.number = number

    def is_even_or_odd(self):
        return "Even" if self.number % 2 == 0 else "Odd"

    def is_prime(self):
        if self.number < 2:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True

    def factorial(self):
        if self.number < 0:
            return "Factorial is not defined for negative numbers."
        result = 1
        for i in range(1, self.number + 1):
            result *= i
        return result

def main():
    while True:
        print("\nNumber Properties")
        print("1. Check if the number is even or odd")
        print("2. Check if the number is prime")
        print("3. Find the factorial of the number")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Error: Please enter a valid integer choice.")
            continue

        if choice == 4:
            print("Goodbye!")
            break

        try:
            number = int(input("Enter a number: "))
            num_prop = NumberProperties(number)

            if choice == 1:
                print(f"The number is {num_prop.is_even_or_odd()}.")
            elif choice == 2:
                print(f"The number is {'Prime' if num_prop.is_prime() else 'Not Prime'}.")
            elif choice == 3:
                print(f"The factorial of the number is {num_prop.factorial()}.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Error: Please enter a valid integer number.")

if __name__ == "__main__":
    main()
