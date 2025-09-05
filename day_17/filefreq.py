filename = "sample.txt"

with open(filename, "r") as file:
    text = file.read().lower()

for ch in ".,!?;:-":
    text = text.replace(ch, "")

words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n" + "="*40)
print("    Word Frequency Counter ")
print("="*40)
for word, count in frequency.items():
    print(f"{word} : {count}")
print("="*40)
