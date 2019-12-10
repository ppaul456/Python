# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341

import matplotlib.pyplot as plt    # using matplotlib module

squares = [1, 4, 9, 16, 25] 

plt.plot(squares) 
plt.show()

plt.plot(squares, linewidth=5)   
# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)
plt.show()

# Correcting the plot
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)
plt.show()




    














