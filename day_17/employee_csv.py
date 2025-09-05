import csv

filename = "employees.csv"

employees = [
    [101, "Alice", 50000],
    [102, "Bob", 60000],
    [103, "Charlie", 55000]
]

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Salary"])  
    writer.writerows(employees)

print(" Employee data written to employees.csv")

print("\n" + "="*40)
print(" Employee Records from CSV")
print("="*40)

with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("="*40)
