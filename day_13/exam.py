score = float(input("Enter your exam score: "))

if score >= 35:
    result = "Pass ✅"
else:
    result = "Fail ❌"

print("\n" + "="*40)
print("          📝 Online Exam Result 📝")
print("="*40)
print(f"Score   : {score}")
print(f"Result  : {result}")
print("="*40)
