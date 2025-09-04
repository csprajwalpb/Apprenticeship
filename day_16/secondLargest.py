def second_largest(numbers):
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return None  
    
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


nums = [12, 45, 7, 45, 89, 23, 89, 10]

result = second_largest(nums)

print("\n" + "="*40)
print("    Second Largest Finder ")
print("="*40)
print("List:", nums)
if result:
    print("Second Largest Number:", result)
else:
    print("Not enough unique numbers in the list.")
print("="*40)
