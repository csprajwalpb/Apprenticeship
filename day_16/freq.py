word = input("Enter a word: ").lower()

frequency = {}

for char in word:
    frequency[char] = frequency.get(char, 0) + 1


print("\n" + "="*40)
print("    Character Frequency Counter ")
print("="*40)
for char, count in frequency.items():
    print(f"{char} : {count}")
print("="*40)
