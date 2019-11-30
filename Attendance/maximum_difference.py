#Pohsun Chang
#830911
#MSITM6341
#12/01/2019


def maximum_difference():                     # Create a function
    lst = []                                  # Create an empty list
    num = int(input("How many numbers? "))
    for i in range(0, num):                   # Use for statement to input numbers into list
        ele = int(input())
        lst.append(ele)
    
    abstract = max(lst) - min(lst)            # Calculate the difference(abstract) between max and min in the list
    print("Maximum difference is: " + str(abstract)) # Print the abstract



maximum_difference()                  # Call the function 


