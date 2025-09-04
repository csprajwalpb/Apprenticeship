grocery_items = [
    "Rice", "Sugar", "Salt", "Milk", "Eggs",
    "Bread", "Butter", "Cheese", "Apples", "Tomatoes"
]

search_item = input("Enter an item to search: ")

if search_item.capitalize() in grocery_items or search_item.lower().capitalize() in grocery_items:
    print(f"\n Yes, '{search_item}' is available in the store.")
else:
    print(f"\n Sorry, '{search_item}' is not available in the store.")
