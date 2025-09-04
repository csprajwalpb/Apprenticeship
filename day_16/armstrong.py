def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    
    total = sum(int(d)**power for d in digits)
    
    return total == num


n = int(input("Enter a number: "))

print("\n" + "="*40)
print("     Armstrong Number Checker ")
print("="*40)

if is_armstrong(n):
    print(f"{n} is an Armstrong number ")
else:
    print(f"{n} is NOT an Armstrong number ")

print("="*40)
