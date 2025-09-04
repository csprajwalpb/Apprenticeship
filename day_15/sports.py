cricket_players = {"Arjun", "Rahul", "Meera", "Priya", "Ananya"}
football_players = {"Karan", "Rahul", "Priya", "Sanjay", "Ananya"}

both = cricket_players.intersection(football_players)

print("\n" + "="*40)
print("    Students Playing Both Sports ")
print("="*40)
if both:
    for student in both:
        print(student)
else:
    print("No student plays both cricket and football.")
print("="*40)
