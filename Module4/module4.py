# Part 1

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        """Default constructor."""
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
    
    def print_item_cost(self):
        """Print Item Cost."""
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${(self.item_price*self.item_quantity):.2f}"

# Part 2

item_count = 2
items = []

for i in range(1,item_count+1):
    print(f"Item {i}")
    print(f"Enter the item name:")
    item_name = str(input())
    print(item_name)
    print(f"Enter the item price:")
    item_price = round(float(input()), 2)
    print(item_price)
    print(f"Enter the item quantity:")
    item_quantity = int(input())
    print(item_quantity)
    items.append(ItemToPurchase(item_name, item_price, item_quantity))

# Step 3

print("TOTAL COST\n")

total = 0
for item in items:
    print(item.print_item_cost(), "\n")
    total += item.item_price*item.item_quantity

print(f"Total: ${total:.2f}")