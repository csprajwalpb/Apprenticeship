# Employee Dictionary Updater

# Initial employee dictionary
employees = {
    "E101": {"name": "Arjun", "designation": "Manager", "salary": 75000},
    "E102": {"name": "Priya", "designation": "Developer", "salary": 55000},
    "E103": {"name": "Rahul", "designation": "Designer", "salary": 50000}
}

# Add a new employee
emp_id = input("Enter new Employee ID: ")
name = input("Enter Employee Name: ")
designation = input("Enter Designation: ")
salary = int(input("Enter Salary: "))

employees[emp_id] = {"name": name, "designation": designation, "salary": salary}

print("\n" + "="*50)
print("    Employee Directory Updated ")
print("="*50)
for eid, details in employees.items():
    print(f"{eid} → {details['name']} | {details['designation']} | ₹{details['salary']}")
print("="*50)
