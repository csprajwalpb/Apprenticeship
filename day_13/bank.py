balance = float(input("Enter initial balance: ₹ "))

interest_rate = 5  

print("\n" + "="*40)
print("        Banking Interest Report ")
print("="*40)

for month in range(1, 13):
    balance += (balance * interest_rate) / 100
    print(f"Month {month}: ₹ {balance:.2f}")

print("="*40)
print("End of 12 Months Statement")
print("="*40)
