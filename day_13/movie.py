ticket_price = 200   
time = int(input("Enter show time (in 24-hour format, e.g., 14 for 2 PM): "))
tickets = int(input("Enter number of tickets: "))

if time < 17:
    discount_rate = 30
    discount = (ticket_price * discount_rate) / 100
    final_price = (ticket_price - discount) * tickets
    category = "Matinee Show (30% Discount)"
else:
    discount_rate = 0
    final_price = ticket_price * tickets
    category = "Regular Show (No Discount)"

print("\n" + "="*40)
print("         Movie Ticket Booking ")
print("="*40)
print(f"Show Time       : {time}:00 hrs")
print(f"Tickets Booked  : {tickets}")
print(f"Category        : {category}")
print(f"Total Amount    : ₹ {final_price:.2f}")
print("="*40)
print("Enjoy your movie! ")
print("="*40)
