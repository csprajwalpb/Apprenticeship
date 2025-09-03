sentence = input("Enter a sentence: ")

cleaned = sentence.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("\n The sentence IS a palindrome!")
else:
    print("\n The sentence is NOT a palindrome.")
