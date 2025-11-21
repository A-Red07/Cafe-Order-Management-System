
"""
Project: Cafe Order Management System
Description: A simple POS system for a cafe. 
Allows users to add items, view bills, and checkout with a timestamp.
"""

import datetime
import random
import array 


MENU = {
    "Coffee": 80.00,
    "Espresso": 120.00,
    "Tea": 50.00,
    "Muffin": 90.00,
    "Croissant": 85.00,
    "Sandwich": 150.00,
    "Water": 60.00
}

current_order = []

STAFF_NAMES = ["Sarah", "Ben", "Chloe", "Mike", "Alex"]


def show_menu_header():
    """Prints the system header with current time and staff name."""
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p") 
    staff = random.choice(STAFF_NAMES)
    
    print("\n" + "="*30)
    print(f" CAFE POS SYSTEM - {time_str}")
    print(f" Cashier on duty: {staff}")
    print("="*30)

def print_main_options():
    """Just shows the numbered options."""
    print("1. Show Menu")
    print("2. Add Item")
    print("3. View Bill")
    print("4. Checkout")
    print("5. Manager Stats (Array Mode)")
    print("6. Exit")
    print("-" * 30)

def show_cafe_menu():
    """Iterates through the menu dict and displays options."""
    print("\n--- MENU ---")
    for item, price in MENU.items():
        # Changed symbol to ₹
        print(f"{item:<12} : ₹{price:.2f}")
    print("-" * 12)

def add_item(order_list):
    """Asks user for an item and adds it to the order if valid."""
    item_input = input("Item name: ").strip().title()

    if item_input in MENU:
        order_list.append(item_input)
        print(f"--> Added 1 {item_input}")
    else:
        print(f"!! Error: '{item_input}' is not on the menu.")

def get_total_price(order_list):
    """
    Calculates total price. 
    Converts the list of prices to a typed array (float) for calculation.
    """
    if not order_list:
        return 0.0
    
    
    prices_list = [MENU[item] for item in order_list]
    
    prices_array = array.array('d', prices_list)
    
    return sum(prices_array)

def print_bill(order_list, is_checkout=False):
    """Displays the current list of items and the total price."""
    print("\n--- RECEIPT ---")
    if not order_list:
        print("(No items added yet)")
        return

    
    for item in order_list:
        print(f"{item:<12} : ₹{MENU[item]:.2f}")
    
    print("-" * 20)
     
    total = get_total_price(order_list)
    print(f"TOTAL        : ₹{total:.2f}")

    if is_checkout:
        
        order_id = random.randint(1000, 9999)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"\nOrder #{order_id} | {timestamp}")
        print("Thank you for visiting!")

def show_manager_stats():
    """
    Calculates basic stats (Avg, Min, Max) about the menu pricing.
    """
    print("\n--- MANAGER STATS ---")
    
    prices = list(MENU.values())
    
   
    price_arr = array.array('d', prices)
    
    total_items = len(price_arr)
    avg_price = sum(price_arr) / total_items
    min_price = min(price_arr)
    max_price = max(price_arr)
    
    print(f"Total Items   : {total_items}")
    print(f"Average Price : ₹{avg_price:.2f}")
    print(f"Lowest Price  : ₹{min_price:.2f}")
    print(f"Highest Price : ₹{max_price:.2f}")

def main():
    while True:
        show_menu_header()
        print_main_options()
        
        choice = input("Select (1-6): ").strip()
        
        if choice == '1':
            show_cafe_menu()
        
        elif choice == '2':
            add_item(current_order)
            
        elif choice == '3':
            print_bill(current_order)
            
        elif choice == '4':
            if current_order:
                print_bill(current_order, is_checkout=True)
                current_order.clear() # Reset for next customer
            else:
                print("Cannot checkout an empty order!")
                
        elif choice == '5':
            show_manager_stats()
            
        elif choice == '6':
            print("System shutting down... Bye!")
            break
        
        else:
            print("Invalid choice, try again.")
            
        input("\n[Press Enter]")

if __name__ == "__main__":
    main()