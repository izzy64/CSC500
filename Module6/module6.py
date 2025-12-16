class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        """Default constructor."""
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = str(item_description)
    
    def print_item_cost(self):
        """Print Item Cost."""
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${(self.item_price*self.item_quantity):.2f}"
    

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2026"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                # Only modify if the new values are not default values
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(item.print_item_cost())
        
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart: ShoppingCart):
    select = ""
    choices = ["a", "r", "c", "i", "o", "q"]
    menu_txt = """
    MENU    
    a - Add item to cart    
    r - Remove item from cart   
    c - Change item quantity    
    i - Output items' descriptions  
    o - Output shopping cart    
    q - Quit    
    Choose an option:  
    """
    while select != "q":
        print(menu_txt)
        select = input()
        
        if select == "a":
            print("ADD ITEM TO CART")
            print("Enter the item name:")
            item_name = input()
            print("Enter the item description:")
            item_description = input()
            print("Enter the item price:")
            item_price = float(input())
            print("Enter the item quantity:")
            item_quantity = int(input())
            
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)
            print("Item added!")
            
        elif select == "r":
            print("REMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            item_name = input()
            cart.remove_item(item_name)
            print("Item removed!")
            
        elif select == "c":
            print("CHANGE ITEM QUANTITY")
            print("Enter the item name:")
            item_name = input()
            print("Enter the new quantity:")
            new_quantity = int(input())
            
            item_to_modify = ItemToPurchase(item_name, 0, new_quantity)
            cart.modify_item(item_to_modify)
            print("Quantity changed!")
            
        elif select == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            
        elif select == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
            
        elif select == "q":
            print("THANKS FOR SHOPPING!")
            pass  # Exit the loop
            
        elif select not in choices:
            print("Invalid option. Please try again.")
        print("\n")


cart = ShoppingCart("John Doe", "February 1, 2020")
print_menu(cart)
