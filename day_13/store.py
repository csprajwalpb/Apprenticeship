purchase = float(input("Enter purchase amount: ₹ "))

if purchase > 5000:
    discount_rate = 20
else:
    discount_rate = 10

discount_amount = (purchase * discount_rate) / 100
final_price = purchase - discount_amount

print("\n" + "="*40)
print("         Online Store Bill         ")
print("="*40)
print(f"Purchase Amount  : ₹ {purchase:.2f}")
print(f"Discount @ {discount_rate}% : -₹ {discount_amount:.2f}")
print("-"*40)
print(f"Final Price      : ₹ {final_price:.2f}")
print("="*40)
