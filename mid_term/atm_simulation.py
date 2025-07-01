class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.withdrawal_limit = 20000  # Daily withdrawal limit
        self.deposit_limit = 50000     # Maximum deposit limit

    def deposit(self, amount):
        if amount > 0:
            if amount <= self.deposit_limit:
                self.balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print(f"Deposit failed! Maximum deposit limit is ₹{self.deposit_limit}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.withdrawal_limit:
                print(f"Withdrawal failed! Maximum withdrawal limit is ₹{self.withdrawal_limit}.")
            elif amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")

# Example usage:
atm = ATM(10000)  # Initial balance

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == 3:
        atm.check_balance()
    elif choice == 4:
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice. Please try again.")
