import matplotlib.pyplot as plt    # using matplotlib module
# Plotting and Styling Individual Points with scatter()
plt.scatter(2, 4) 
plt.show()
plt.scatter(2, 4, s=200)
# Set chart title and label axes. 
plt.title("Square Numbers", fontsize=24) 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels. 
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

#Plotting a Series of Points with scatter()
x_values = [1, 2, 3, 4, 5] 
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
plt.show()

#Calculating Data Automatically
x_values = list(range(1, 1001)) 
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)
# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])
plt.show()

#Removing Outlines from Data Points
plt.scatter(x_values, y_values, edgecolor='none', s=40)

#Defining Custom Colors
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
#Using the RGB color model(light blue)
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

#Using a Colormap
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.show()

#Saving Your Plots Automatically 
plt.savefig('squares_plot.png', bbox_inches='tight')