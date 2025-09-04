def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)

print("\n" + "="*40)
print("    Greatest Common Divisor (GCD) ")
print("="*40)
print(f"Numbers : {num1} and {num2}")
print(f"GCD      : {result}")
print("="*40)
