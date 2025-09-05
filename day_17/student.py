filename = "attendance.txt"

date = input("Enter today's date (DD-MM-YYYY): ")
student_name = input("Enter student name: ")
status = input("Enter status (Present/Absent): ")

with open(filename, "a") as file:
    file.write(f"{date} - {student_name} : {status}\n")

print(" Attendance updated successfully!")

print("\n Attendance Records:")
print("="*40)
with open(filename, "r") as file:
    print(file.read())
print("="*40)
