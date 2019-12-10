# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341
import pygal
from die import Die
# Create a D6
die = Die()
# Make some rolls, and store results in a list.
results = [] 

for roll_num in range(1000):    
    result = die.roll()    
    results.append(result)    
    # Analyze the results. 
    frequencies = [] 
    for value in range(1, die.num_sides+1): 
        frequency = results.count(value)
        frequencies.append(frequency)    
    
    # Visualize the results. 
    hist = pygal.Bar()        # a bar chart by creating an instance of pygal.Bar()
    hist.title = "Results of rolling one D6 1000 times." 
    hist.x_labels = ['1', '2', '3', '4', '5', '6'] 
    hist.x_title = "Result" 
    hist.y_title = "Frequency of Result"
    
    #Passing a label for the set of values to be added and a list of the values to appear on the chart
    hist.add('D6', frequencies) 
    hist.render_to_file('die_visual.svg')






