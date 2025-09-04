vehicles = set()
n = int(input("Enter how many vehicles to register: "))

for i in range(n):
    vehicle = input(f"Enter vehicle number {i+1}: ").upper()
    if vehicle in vehicles:
        print(f" {vehicle} is already registered. Duplicate not allowed.")
    else:
        vehicles.add(vehicle)
        print(f" {vehicle} registered successfully.")

print("\n" + "="*40)
print("    Registered Vehicle Numbers ")
print("="*40)
for v in vehicles:
    print(v)
print("="*40)
