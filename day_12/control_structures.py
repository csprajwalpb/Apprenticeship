print("=== Conditional Statements ===")

temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's pleasant outside!")

score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Score: {score}, Grade: {grade}")

print("\n=== Loop Structures ===")

print("For loop with range:")
for i in range(5):
    print(f"Iteration {i}")

print("\nFor loop with list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\nFor loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index+1}. {fruit}")

print("\nWhile loop:")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

print("\nNested loops:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

print("\nBreak statement example:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print() 

print("\nContinue statement example:")
print("Odd numbers from 0 to 9:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()  

print("\n=== Nested Conditionals ===")
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a license first!")
else:
    print("You are not old enough to drive!")