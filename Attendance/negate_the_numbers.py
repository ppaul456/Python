#Pohsun Chang
#830911
#MSITM6341
#10/29/2019

mylist = [ 1, 2, 3, -7]
print(mylist)

# adding "-" front of the list and loop the range of mylist
# mylist's numbers will all be negated
for i in range(len(mylist)):
    mylist[i] = -mylist[i]
print(mylist)