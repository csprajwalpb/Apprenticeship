students = {
    "Arjun": 85,
    "Priya": 92,
    "Rahul": 78,
    "Meera": 95,
    "Karan": 88
}

topper = max(students, key=students.get)

print("\n" + "="*40)
print("   Topper Finder ")
print("="*40)
print("Students & Marks:")
for name, marks in students.items():
    print(f"{name} : {marks}")

print("-"*40)
print(f"Topper is {topper} with {students[topper]} marks ")
print("="*40)
