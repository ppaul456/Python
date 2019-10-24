#Pohsun Chang
#830911
#MSITM6341
#10/29/2019

random_numbers = [2, 14, 5, 10, 28, 11]
current_max_num = random_numbers[0]

for number in random_numbers:
    if number > current_max_num:
        current_max_num = number
# using for loop to find the largest element in the list
# will keep looping until it finds the maximum num
print(current_max_num)
