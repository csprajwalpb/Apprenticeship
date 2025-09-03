print("Enter marks out of 100 for 5 subjects:")
sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print("\n" + "="*40)
print("          📘 School Report 📘")
print("="*40)
print(f"Total Marks   : {total}/500")
print(f"Percentage    : {percentage:.2f}%")
print(f"Grade         : {grade}")
print("="*40)
