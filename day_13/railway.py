name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))

full_ticket_price = 100  

if age < 5:
    fare = 0
    category = "Free Ticket"
elif age <= 60:
    fare = full_ticket_price
    category = "Full Ticket"
else:
    fare = full_ticket_price / 2
    category = "Half Ticket"

print("\n" + "="*40)
print("         Railway Reservation ")
print("="*40)
print(f"Passenger Name : {name}")
print(f"Age            : {age}")
print(f"Category       : {category}")
print(f"Fare           : ₹ {fare:.2f}")
print("="*40)
print("Have a safe journey!")
print("="*40)
