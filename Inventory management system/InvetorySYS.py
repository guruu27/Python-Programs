'''
You are given a basic inventory management system written in Python. Your task is to enhance its functionality by adding new features and improving error handling.

Tasks

Add Item Removal Feature:

Update the menu with an option to remove items from the inventory.

Implement functionality allowing users to specify the item name and quantity to remove.

Implement Error Handling:



Ensure that the user inputs a valid positive integer for both adding and removing items.

Catch and handle any exceptions that might occur due to invalid inputs.

Stock Warning Message:

Modify the program to display a warning if the user attempts to remove more items than are available in stock.

Implement Item Search:

Add a menu option that allows users to search for a specific item in the inventory.

If the item exists, display its quantity; if not, inform the user that the item is not in stock.

Create Total Inventory Function:



Write a new function that calculates the total number of items in the inventory.

Add an option to the menu to display this total count to the user.

def display_menu():
 print("\nInventory Management System") 
 print("1. Add item") 
 print("2. Remove item") 
 print("3. Search for item")
 print("4. Display total number of items")
 print("5. Exit")
 
 
'''
# Inventory Management System

inventory = {}

def display_menu():
    print("\nInventory Management System")
    print("1. Add item")
    print("2. Remove item")
    print("3. Search for item")
    print("4. Display total number of items")
    print("5. Exit")

def add_item():
    try:
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        if quantity > 0:
            if item_name in inventory:
                inventory[item_name] += quantity
            else:
                inventory[item_name] = quantity
            print(f"{quantity} {item_name}(s) added to inventory.")
        else:
            print("Quantity must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for quantity.")

def remove_item():
    try:
        item_name = input("Enter item name to remove: ")
        quantity_to_remove = int(input("Enter quantity to remove: "))
        if quantity_to_remove > 0:
            if item_name in inventory:
                if quantity_to_remove <= inventory[item_name]:
                    inventory[item_name] -= quantity_to_remove
                    print(f"{quantity_to_remove} {item_name}(s) removed from inventory.")
                else:
                    print("Not enough stock to remove. Please check the quantity.")
            else:
                print("Item not found in inventory.")
        else:
            print("Quantity to remove must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for quantity to remove.")

def search_item():
    item_name = input("Enter item name to search: ")
    if item_name in inventory:
        print(f"{item_name} quantity: {inventory[item_name]}")
    else:
        print(f"{item_name} not found in inventory.")

def display_total_items():
    total_items = sum(inventory.values())
    print(f"Total number of items in inventory: {total_items}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            search_item()
        elif choice == "4":
            display_total_items()
        elif choice == "5":
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
