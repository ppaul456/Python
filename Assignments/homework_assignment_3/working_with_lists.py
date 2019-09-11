#Pohsun Chang
#830911
#MSITM6341
#09/17/2019
grocery_items = ['Apple','Orange', 'Steak', 'Chicken', 'water']
# create 5 items in a list
price_of_grocery_items = [40,30,60,50,10]
# ceate each item's price in another list
print(grocery_items)
print(price_of_grocery_items)

print(grocery_items[2]+' costs $'+str(price_of_grocery_items[2]))
#Print the 3rd item followed by it’s price 
print(grocery_items[-1]+' costs $'+str(price_of_grocery_items[-1]))
#Print the last item followed by it’s price

grocery_items.append('watermelon')
price_of_grocery_items.append(25)
#add something to the last(append)
print(grocery_items)
print(price_of_grocery_items)

del grocery_items[0]
del price_of_grocery_items[0]
#delete [0] elements from both lists

price_of_grocery_items[1] = 120
#Double the price of the 2nd item

print(grocery_items)
print(price_of_grocery_items)
