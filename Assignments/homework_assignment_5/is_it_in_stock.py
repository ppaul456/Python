#Pohsun Chang
#830911
#MSITM6341
#09/31/2019

menu_items_in_stock = ["Tacos", "Chips", "Salsa", "Quesadilla"]
customer_order = ["Tacos", "Guacamole", "Burrito", "Chips", "Salsa"]
# change lists to lowercase
menu_items_in_stock = [l.lower() for l in menu_items_in_stock ] 
customer_order = [l.lower() for l in customer_order ]



# use for loop and see if the item is in stock
for item in customer_order:
    if item in menu_items_in_stock:
        print("We have" + " " + item + " " + "in stock")
    else:
        print("We do not have" + " " + item + " " + "in stock")
    








