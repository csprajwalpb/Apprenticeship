item_cost = float(input("Enter the cost of the item: ₹ "))

gst_rate = 18

gst_amount = (item_cost * gst_rate) / 100
final_bill = item_cost + gst_amount

print("\n" + "="*40)
print("          Restaurant Bill          ")
print("="*40)
print(f"Item Cost         : ₹ {item_cost:.2f}")
print(f"GST @ {gst_rate}%      : ₹ {gst_amount:.2f}")
print("-"*40)
print(f"Final Bill Amount : ₹ {final_bill:.2f}")
print("="*40)
