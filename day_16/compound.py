def compound_interest(principal, rate, time, n=1):
    """
    principal : Initial amount
    rate      : Annual interest rate in %
    time      : Time in years
    n         : Number of times interest applied per year (default = 1)
    """
    amount = principal * (1 + (rate / 100) / n) ** (n * time)
    ci = amount - principal
    return ci, amount


P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
T = int(input("Enter Time (in years): "))
N = int(input("Enter compounding frequency per year: "))

ci, final_amount = compound_interest(P, R, T, N)

print("\n" + "="*40)
print("     Compound Interest Calculator ")
print("="*40)
print(f"Principal        : ₹{P}")
print(f"Rate of Interest : {R}%")
print(f"Time             : {T} years")
print(f"Compounding/Year : {N}")
print("-"*40)
print(f"Final Amount     : ₹{final_amount:.2f}")
print(f"Compound Interest: ₹{ci:.2f}")
print("="*40)
