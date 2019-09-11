
grocery_items = ['Apple','Orange', 'Steak', 'Chicken', 'water']

number_of_grocery_items = [4,3,6,5,4,2400]

print(grocery_items)
print(number_of_grocery_items)

print(grocery_items[0])      
#index 0
print(grocery_items[-1])
# index-1 = the last
print(grocery_items[-3])

grocery_items[1]= 'Pear'
#change [1] to Pear
print(grocery_items[1])

grocery_items.append('watermelon')
#add something(append)
print(grocery_items)
  
grocery_items.insert(1,'Pineapple')
#insert Pineapple to [1]
grocery_items.insert(7,'Pineapple')
#insert can pass the index[0~6] be the last
print(grocery_items)

del grocery_items[4]
#delete [4]
print(grocery_items)

grocery_items.remove('Pear')
#remove the particular element
print(grocery_items)

grocery_items.remove('Pineapple')
#remove the first Pineapple
print(grocery_items)

