sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

count = 0
for char in sentence:
    if char in vowels:
        count += 1

print("\n" + "="*40)
print("        Vowel Counter ")
print("="*40)
print(f"Sentence: {sentence}")
print(f"Total Vowels: {count}")
print("="*40)
