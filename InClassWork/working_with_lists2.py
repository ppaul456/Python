grocery_items = ['Apple','Orange', 'Steak', 'Chicken', 'Water']

grocery_items.sort()
# set in orders
print (grocery_items)

grocery_items.reverse()
# set in opposite orders
print (grocery_items)

grocery_items_sorted = sorted(grocery_items) 
# same information but use sorted to reorder and save in grocery_items_sorted
print (grocery_items)

print(len(grocery_items))
# count elements

print(grocery_items[1:3])
# print [1]and[3-1](endindex-1) elements
print(grocery_items[3:])
# print [3] till the end elements

for item in grocery_items:
    print(item)
    print(item)
# (for in) putting elements into "item"             