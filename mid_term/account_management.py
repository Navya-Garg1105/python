class BankAccount:
    def __init__(self, account_number, balance):
        self.acc_no = account_number
        self.bal = balance

    def deposit(self, amount):
        self.bal += amount
        print("deposited")

    def withdraw(self, amount):
        if amount > self.bal:
            print("insufficient Balance")
        else:
            self.bal -= amount
            print("withdraw")
    def get_balance(self):
        return self.bal

# Example usage:
accno = int(input("enter account number"))
bal = float(input("enter balance "))
obj = BankAccount(accno, bal)
# Create an account and perform transactions
while True:
    choice = input("enter choice  deposit/ withdraw/ getbalance/ exit").strip().lower()
    if choice =='deposit':
        amt = float(input("enter amount "))
        obj.deposit(amt)
    if choice == 'withdraw':
        amt = float(input("enter amount "))
        obj.withdraw(amt) 
    if choice =='getbalance':
        print(obj.get_balance)
    if choice == 'exit':
        print("exiting")
        break
    else :
        print("invalid choice")