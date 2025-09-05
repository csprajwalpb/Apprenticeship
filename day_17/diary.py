from datetime import datetime

filename = "diary.txt"

note = input("Write your diary entry: ")

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
entry = f"\n[{today}] {note}\n"

with open(filename, "a") as file:
    file.write(entry)

print("\n" + "="*40)
print("    Diary Updated Successfully ")
print("="*40)
print(f"Your entry was saved in '{filename}'")
print("="*40)
