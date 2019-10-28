#Pohsun Chang
#830911
#MSITM6341
#10/29/2019

# define a function for finding out the length
def string_length(the_string):
    counter = 0
    for char in the_string:
        counter+=1
    return counter

# user input
the_string = input("enter string :")
length = string_length(the_string)
print("length is ", length)
