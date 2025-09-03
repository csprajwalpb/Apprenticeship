num = int(input("Enter a number to print its multiplication table: "))

print("\n" + "="*40)
print(f"      Multiplication Table of {num} ")
print("="*40)

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("="*40)
