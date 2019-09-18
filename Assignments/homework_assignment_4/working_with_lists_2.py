#Pohsun Chang
#830911
#MSITM6341
#09/17/2019

odd_list = [num for num in range(3, 50 + 1) if num % 2 != 0]
# assign odd numbers from the range 3 to 50 into the list
print(odd_list)
# make sure it prints out the correct odd numbers 

x = 0
# while loop to print the odd numbers from index 0-4
while(x < 5):     
    # checking condition(print the first 5 numbers) 
       print(odd_list[x]) 
       x += 1
    