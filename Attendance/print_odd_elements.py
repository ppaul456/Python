#Pohsun Chang
#830911
#MSITM6341
#10/29/2019

random_numbers = [2, 14, 5, 10, 28, 11]
odd_number = []
count = 0
print(random_numbers[1])

for count in range(0, len(random_numbers)):  
    if count %2 != 0:
        odd_number.append(random_numbers[count])
        count = count +1 
print(odd_number)
            