people = [
    ("Arjun", 16),
    ("Priya", 22),
    ("Rahul", 18),
    ("Meera", 25),
    ("Karan", 14),
    ("Ananya", 30)
]

adults = [person for person in people if person[1] > 18]

print("\n" + "="*40)
print("    People Above 18 ")
print("="*40)
for name, age in adults:
    print(f"{name} ({age} years)")
print("="*40)
