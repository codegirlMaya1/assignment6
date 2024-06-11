# The aim of this assignment is to create a program that helps users make a shopping list.
purchase_list = []


# Function to help user complete shopping task
def get_help():
    print(" Enter one item at a time or type HELP....")
    print(""" Please Enter DONE when you have your items.
Enter 'HELP' for additional info. Enter YES to remove your last added item....
Enter 'See List' to show your list. Go ahead and type an item to add to your list below....""" )
    

# Task 1: Write a function that lets the user add items to a list.
def add_to_list(item):
    purchase_list.append(item)
    print(f"{item} was added to your shopping list!")
    print(f"You have {len(purchase_list)} items on your list.")
#Task 2: Include a feature to remove items from the list.
def  remove_item():
    purchase_list.pop()
print(f"{remove_item} was removed from  your shopping list!")
print(f"You have {len(purchase_list)} items on your list.")

    
#Task 3: Add a function that prints out the entire list in a formatted way.
# Function to print all out all items currently in the shopping list
def see_list():
    print("My Shopping List:")
    for item in purchase_list:
        print(item)

# Display initial help information
get_help()

# Main loop for user interaction
while True:
    new_item = input("> ")

    # If the user inputs 'DONE', breaks the loop
    if new_item == "DONE":
        break
    # If the user inputs 'HELP', will print the help information provided
    elif new_item == "HELP":
        get_help()
        continue
    elif new_item== "YES":
        remove_item()
        print ("The last item you added was removed from your shopping list")
        continue
    # If the user inputs 'See List',  will show the list
    elif new_item == "See List":
        see_list()
        continue
    # Otherwise, will add the item to the list individually
    add_to_list(new_item)

# Display the final shopping list
see_list()

