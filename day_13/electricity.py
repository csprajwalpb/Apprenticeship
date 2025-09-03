units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

print("\n" + "="*40)
print("         Electricity Bill ")
print("="*40)
print(f"Units Consumed : {units}")
print(f"Total Bill     : ₹ {bill:.2f}")
print("="*40)
