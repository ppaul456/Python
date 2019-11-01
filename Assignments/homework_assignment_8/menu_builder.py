#Pohsun Chang
#830911
#MSITM6341
#11/05/2019

menu_items = {}

# Use boolean to assign should_ask_for_item as True
should_ask_for_item = True

# define the function for inputing item's name 
def ask_user_for_menu_item_name():
    item = input("Item Name: ")
    return item

# define the function for inputing item's cost 
def ask_user_for_menu_item_cost():
    cost = input("Item Cost: ")
    return cost
    
# define the function for adding item and cost into menu_items and show the warning if the item alreay sxists
def add_menu_item(menu_items, item, cost):
    if item in menu_items:
        print("WARNING: Item exists")
    menu_items[item] = cost

print("----------------------------")
print("Please enter the menu items for the Restaurant")
print("----------------------------")

while should_ask_for_item:
# assign item and cost's values from first two functions
    item = ask_user_for_menu_item_name()
    cost = ask_user_for_menu_item_cost()
    
    add_menu_item(menu_items, item, cost)
    
    continue_or_not = input("Continue(Y/N)? ")

    if continue_or_not == "N":
        should_ask_for_item = False
 # assign N as Fasle and end the loop

print("----------------------------")
print("Restaurant Menu")
print("----------------------------")

# Use default method items() to fetch the values of item and cost from menu_items 
for item, cost in menu_items.items():
    print("Item: " + item + " Cost: " + cost)

print("----------------------------")




