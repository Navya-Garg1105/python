class Order:
    def __init__(self):
        self.products = {}  # Dictionary to store products and their prices

    def add_product(self, product, price):
        if product in self.products:
            print(f"Product '{product}' is already in the order.")
        else:
            self.products[product] = price
            print(f"Added '{product}' to the order for ₹{price}.")

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]
            print(f"Removed '{product}' from the order.")
        else:
            print(f"Product '{product}' not found in the order.")

    def calculate_total(self):
        total = sum(self.products.values())
        print(f"Total cost of the order: ₹{total}")

# Example usage:
order = Order()

while True:
    print("\n1. Add Product\n2. Remove Product\n3. Calculate Total\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))
        order.add_product(product, price)
    elif choice == 2:
        product = input("Enter product name to remove: ")
        order.remove_product(product)
    elif choice == 3:
        order.calculate_total()
    elif choice == 4:
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
