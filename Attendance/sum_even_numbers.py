#Pohsun Chang
#830911
#MSITM6341
#10/29/2019

# Python Program to Calculate Sum of Even Numbers from 1 to N
 
n=int(input('Enter the number:'))
if(n>0):
    sum=0
    x = 0
    for x in range(0,n+1):
        if(x % 2 == 0):
            sum=sum+x
            
print(sum)
