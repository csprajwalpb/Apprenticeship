marks = []
print("Enter marks for 5 subjects:")

for i in range(1, 6):
    mark = float(input(f"Subject {i}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("\n" + "="*40)
print("         Marks Management ")
print("="*40)
print(f"Marks Entered : {marks}")
print(f"Highest Mark  : {highest}")
print(f"Lowest Mark   : {lowest}")
print(f"Average Marks : {average:.2f}")
print("="*40)
