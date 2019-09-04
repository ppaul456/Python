#Pohsun Chang
#830911
#MSITM6341
#09/10/2019
Symbol = 'AAPL'
Price = 204.66
Change = -4.08
# Define three variables: Symbol,Price,Change
print("Symbal:" + Symbol + "," + "Price:" + str(Price) + ","+ "Change:" + str(Change) + "\n")
#print out variables and convert Price and Change to string so they can combine

Symbol = 'aappl'
#rename Symbol
Price = '$204.66'
#redefine Price to string
print("Symbal:" + Symbol + "," + "Price:" + Price + ","+ "Change:" + str(Change) + "\n")
#combine them and print out

Symbol = 'AAPL'
#rename Symbol back
Price = 204.66
#redefine Price back to float
print("Symbal:" + Symbol + "---" + "Yesterday’s Price:" + str("%.2f"%((Price+Change))))
#combine them and use "%.2f"%() constraining Price+Change for two decimal places, and convert it to string 