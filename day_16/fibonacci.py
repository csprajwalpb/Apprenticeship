def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Enter number of terms: "))

print("\n" + "="*40)
print("    Fibonacci Series (Recursive) ")
print("="*40)
for i in range(num):
    print(fibonacci(i), end=" ")
print("\n" + "="*40)
