items = {
    "apple": 120,
    "banana": 50,
    "milk": 60,
    "bread": 40,
    "rice": 80
}

print("\nAvailable Items:")
for item, price in items.items():
    print(f"{item.capitalize()} → ₹{price}")

cart = {}
while True:
    product = input("\nEnter product name (or 'done' to finish): ").lower()
    if product == "done":
        break
    if product in items:
        qty = int(input(f"Enter quantity of {product}: "))
        cart[product] = cart.get(product, 0) + qty
    else:
        print(" Item not available.")

total = sum(items[p] * q for p, q in cart.items())

print("\n" + "="*40)
print("           Final Bill ")
print("="*40)
for product, qty in cart.items():
    print(f"{product.capitalize()} x {qty} = ₹{items[product] * qty}")
print("-"*40)
print(f"Total Amount : ₹{total}")
print("="*40)
