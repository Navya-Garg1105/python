class Item:
    def __init__(self, name, price):
        self.name  = name 
        self.price  = price

class ShoppingCart:
    def __init__(self):
        self.lst = []

    def add_item(self, name, price):
        item = Item(name, price )
        self.lst.append(item)
        print(f"{name} addes to list")

    def remove_item(self, name):
        for item in self.lst:
            if name == name :
                self.lst.remove(name)
                print(f"{name} removed from the list")

    def total_price(self):
        self.total = 0
        for price in self.lst:
            self.total += price 
        print(self.total)

# Example usage:
cart = ShoppingCart()
# Reading input and performing operations
while True:
    operation = input("Enter operation (add/remove/total/exit): ").strip().lower()

    if operation == "add":
        name = input("Enter item name: ").strip()
        price = float(input("Enter item price: "))
        cart.add_item(name, price)

    elif operation == "remove":
        name = input("Enter item name to remove: ").strip()
        cart.remove_item(name)

    elif operation == "total":
        cart.total_price()

    elif operation == "exit":
        print("Exiting shopping cart.")
        break

    else:
        print("Invalid operation. Try again.")
