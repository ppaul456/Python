#Pohsun Chang
#830911
#MSITM6341
#09/10/2019
Symbol = 'AAPL'
Price = 204.66
Change = -4.08
# Define three variables: Symbol,Price,Change
print("Symbol:" + Symbol + "," + "Price:" + str(Price) + ","+ "Change:" + str(Change) + "\n")
#print out variables and convert Price and Change to string so they can combine

print("Symbol:" + Symbol.lower() + "," + "Price:$" + str(Price) + ","+ "Change:" + str(Change) + "\n")
#turn AAPL to lowercase, combine them and print out

print("Symbol:" + Symbol + "---" + "Yesterday’s Price:" + str("%.2f"%((Price+Change))))
#combine them and use "%.2f"%() constraining Price+Change for two decimal places, and convert it to string 