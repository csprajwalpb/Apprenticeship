paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

clean_words = [word.strip(".,!?;:") for word in words]

unique_words = set(clean_words)

print("\n" + "="*40)
print("   Unique Word Counter ")
print("="*40)
print(f"Total Words       : {len(clean_words)}")
print(f"Unique Words      : {len(unique_words)}")
print("Unique Word List  :", unique_words)
print("="*40)
