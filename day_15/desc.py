salaries = [35000, 55000, 42000, 70000, 28000, 60000]

salaries.sort(reverse=True)

print("\n" + "="*40)
print("   Employee Salary Sorter ")
print("="*40)
print("Sorted Salaries (High → Low):")
for s in salaries:
    print(f"₹ {s}")
print("="*40)
