# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk() 
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15) 
plt.show()

#Generating Multiple Random Walks 
# Keep making new walks, as long as the program is active. 
while True: 
    rw = RandomWalk() 
    rw.fill_walk()
    #Coloring the Points 
    point_numbers = list(range(rw.num_points))    
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15) 
    
    #Plotting the Starting and Ending Points
    #Emphasize the first and last points.    
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)    
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #Cleaning Up the Axes 
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)    
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    keep_running = input("Make another walk? (y/n): ")    
    if keep_running == 'n':        
        break

#Adding Plot Points 
while True: 
    # Make a random walk, and plot the points
    rw = RandomWalk(50000) 
    rw.fill_walk()
    
    #Altering the Size to Fill the Screen
    #Set the size of the plotting window.    
    plt.figure(figsize=(10, 6))
    
    # Plot the points, and show the plot
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)    
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")    
    if keep_running == 'n':        
        break



