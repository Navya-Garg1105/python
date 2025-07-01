class BankAccount:
    def __init__(self, account_holder_name, starting_balance=0):
        self.account_holder_name = account_holder_name
        self.balance = starting_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        self.balance += amount
        return f"Successfully deposited {amount}. Current balance: {self.balance}."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient balance for this withdrawal."
        self.balance -= amount
        return f"Successfully withdrew {amount}. Current balance: {self.balance}."

def main():
    print("Welcome to the Bank Account Management System")
    name = input("Enter your name: ")
    try:
        starting_balance = float(input("Enter your starting balance: "))
    except ValueError:
        print("Invalid input. Starting balance set to 0.")
        starting_balance = 0

    account = BankAccount(name, starting_balance)

    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print(f"Your current balance is: {account.check_balance()}")
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to deposit: "))
                print(account.deposit(amount))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 3:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                print(account.withdraw(amount))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 4:
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
