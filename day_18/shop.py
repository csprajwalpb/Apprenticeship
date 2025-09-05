class ShoppingCart:
    def __init__(self):
        self.cart = {}  

    def add_item(self, item, price):
        if item in self.cart:
            self.cart[item] += price
        else:
            self.cart[item] = price
        print(f" Added {item} for ₹{price}")

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]
            print(f" Removed {item}")
        else:
            print(f" {item} not found in cart.")

    def display_cart(self):
        if not self.cart:
            print("\n Cart is empty.")
            return
        print("\n Shopping Cart:")
        print("="*40)
        total = 0
        for item, price in self.cart.items():
            print(f"{item} : ₹{price}")
            total += price
        print("="*40)
        print(f"Total Bill: ₹{total}")
        print("="*40)


cart = ShoppingCart()
cart.add_item("Apples", 120)
cart.add_item("Milk", 50)
cart.add_item("Bread", 40)

cart.display_cart()

cart.remove_item("Milk")
cart.display_cart()
