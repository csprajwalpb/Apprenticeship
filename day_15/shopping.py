list1 = ["Milk", "Eggs", "Bread", "Rice", "Sugar"]
list2 = ["Sugar", "Salt", "Butter", "Milk", "Cheese"]

merged_list = list(set(list1 + list2))

print("\n" + "="*40)
print("       Merged Shopping List ")
print("="*40)
print("List 1:", list1)
print("List 2:", list2)
print("-"*40)
print("Final Merged List (No Duplicates):")
print(merged_list)
print("="*40)
