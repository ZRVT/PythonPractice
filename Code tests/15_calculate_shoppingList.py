def calculate_item_total(quantity, price_per_unit):
    """Calculate the total cost for an individual item."""
    return quantity * price_per_unit

shopping_list = []  # To store all items
total_cost = 0  # To calculate the total price

while True:
    item_name = input("Enter the item name: ")
    
    try:
        quantity = float(input("Enter the quantity: "))
        price_per_unit = float(input("Enter the price per unit: "))
    except ValueError:
        print("Please enter valid numbers for quantity and price.")
        continue

    item_total = calculate_item_total(quantity, price_per_unit)
    shopping_list.append({"name": item_name, "quantity": quantity, "price": price_per_unit, "total": item_total})
    total_cost += item_total

    another_item = input("Do you want to add another item? (yes/no): ").strip().lower()
    if another_item != "yes":
        break

print("\nYour Shopping List:")
for item in shopping_list:
    print(f"{item['name']}: {item['quantity']} units at ${item['price']} each. Total = ${item['total']:.2f}")

print(f"\nTotal price of your shopping list is: ${total_cost:.2f}")
