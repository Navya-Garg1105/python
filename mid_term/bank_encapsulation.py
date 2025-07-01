class BankAccount:
    def __init__(self, initial_balance):
        # Initialize balance privately
        self.initial = initial_balance
    
    def deposit(self, amount):
        # Add to balance
        self.initial = self.initial + amount
    
    def withdraw(self, amount):
        # Subtract from balance (no overdraft)
        self.initial -= amount 
    
    # Implement this
    def get_balance(self):
        return self.initial

# Test Input
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())  # Expected Output: 120