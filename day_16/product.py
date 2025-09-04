products = {
    "apple": 120,
    "banana": 50,
    "milk": 60,
    "bread": 40,
    "rice": 80,
    "eggs": 90
}

product_name = input("Enter product name: ").lower()

print("\n" + "="*40)
print("   Product Price Finder ")
print("="*40)
if product_name in products:
    print(f"Price of {product_name.capitalize()} : ₹ {products[product_name]}")
else:
    print(f" Sorry, {product_name.capitalize()} not found in store.")
print("="*40)
