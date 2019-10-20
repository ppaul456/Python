#Pohsun Chang
#830911
#MSITM6341
#10/22/2019

menu_items_price = {'Chicken': 10.0, 'Corn': 5.0, 'Fried Rice': 15.0, 'Salad': 6.0,'Mashed Potatoes': 5.0}
# create a dict for items and their prices

customer_order = ['Chicken', 'Pork', 'Mashed Potatoes']
# create a list for customer's orders

# use for and if esle to set the condisiotn for print out
for item in customer_order:
    if menu_items_price.get(item):
        print('$' + str(menu_items_price[item]))
    else:
        print("We do not have" + " " + item + " " + "in stock")
print("-----------------------")

print("Total price: " + "$" +str(menu_items_price.get(customer_order[0]) + menu_items_price.get(customer_order[2])))
# calculate the total price-1(just add those two values)

# calculate the total price-2(using for and if statement)
total_price = []

for price in customer_order:
    if menu_items_price.get(price):
        price = menu_items_price[price]
        total_price.append(price)

print("Total price: $" + str(sum(total_price)))


    