class PaymentMethod:
    def pay(self, amount):
        self.amount = amount

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f'payment of {amount} done by credit card')

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f'payment of {amount} done  by Debit card') 

class Cash(PaymentMethod):
    def pay(self, amount):
        print(f'payment of {amount} done  by Cash ')

# Example usage:
amount = int(input())
# Call the pay method for each payment type
credit = CreditCard()
credit.pay(amount)
debit = DebitCard()
debit.pay(amount)
cash =Cash()
cash.pay(amount)



