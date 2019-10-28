#Pohsun Chang
#830911
#MSITM6341
#10/29/2019

menu_items_price = {'Chicken': 10.0, 'Corn': 5.0, 'Fried Rice': 15.0, 'Salad': 6.0,'Mashed Potatoes': 5.0}
# create a dict for items and their prices
customer_order = []
# create an emty list for customer's orders

for input_item in range(0, len(menu_items_price)):
    input_item = input("Enter an item ")
    customer_order.append(input_item)
# for loop to append user input to the list of customer_order   

# use for and if esle to set the condisiotn for the item's cost or "we do not have"
for item in customer_order:
    if menu_items_price.get(item):
        print(item + ": " + "$" + str(menu_items_price[item]))
    else:
        print("We do not have" + " " + item + " " + "in stock")
print("-----------------------")


# calculate the total price(using for and if statement)
total_price = []

for price in customer_order:
    if menu_items_price.get(price):
        price = menu_items_price[price]
        total_price.append(price)

print("Total price: $" + str(sum(total_price)))