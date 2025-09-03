num = int(input("Enter a number to find its factorial: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("\n" + "="*40)
print(f" Factorial of {num} = {factorial}")
print("="*40)
