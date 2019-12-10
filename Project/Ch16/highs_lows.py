# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341

#Parsing the CSV File Headers
#Printing the Headers and Their Positions
import csv

filename = 'sitka_weather_07-2014.csv' 

with open(filename) as f:
    #call csv.reader() to create a reader object associated with that file
    reader = csv.reader(f)   
    header_row = next(reader) # next() function returns the next line in the file when passed the reader object. 
    # We call next() only once so we get the first line of the file, which contains the file headers   
    for index, column_header in enumerate(header_row):  # use enumerate() on the list to get the index of each item, and the value      
        print(index, column_header)

# Get high temperatures from file. 
with open(filename) as f:    
    reader = csv.reader(f)    
    header_row = next(reader) 
    highs = []
    for row in reader:       
        high = int(row[1])   # convert str to int for pyplot to read
        highs.append(high)            
    #print(highs)


#Plotting Data in a Temperature Chart
#Plotting Dates
#Plotting a Longer Timeframe
#Get dates, high, and low temperatures from file
#Shading an Area in the Chart 
from matplotlib import pyplot as plt
from datetime import datetime
# Get dates and high temperatures from file
filename = 'sitka_weather_2014.csv' 
with open(filename) as f:    
    reader = csv.reader(f)    
    header_row = next(reader) 
    dates, highs, lows = [], [], []
    for row in reader:       
        current_date = datetime.strptime(row[0], "%Y-%m-%d") # call the method strptime() with the string containing the date we want to work, and how the date is formatted        
        dates.append(current_date)
        
        high = int(row[1])
        highs.append(high)  

        low = int(row[3])
        lows.append(low)             
    # Plot data. 
    fig = plt.figure(dpi=128, figsize=(10, 6))  
    plt.plot(dates, highs, c='red', alpha=0.5) #alpha controls a color’s transparency
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # facecolor determines the color of the shaded region 
    # Format plot.
    plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16) 
    fig.autofmt_xdate() # draws the date labels diagonally to prevent them from overlapping
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()

#Error-Checking 
#Missing data can result in exceptions that crash our programs if we don’t handle them properly
# Get dates, high, and low temperatures from file. 
filename = 'death_valley_2014.csv' 
with open(filename) as f:
    reader = csv.reader(f)    
    header_row = next(reader) 
    dates, highs, lows = [], [], []
    for row in reader:         
        try:            
            current_date = datetime.strptime(row[0], "%Y-%m-%d")            
            high = int(row[1])            
            low = int(row[3])        
        except ValueError:     # If any data is missing, Python will raise a ValueError         
            print(current_date, 'missing data')  #Printing an error message that includes the date of the missing data       
        else: 
            dates.append(current_date)            
            highs.append(high)            
            lows.append(low)
    # Plot data. 
    fig = plt.figure(dpi=128, figsize=(10, 6))  
    plt.plot(dates, highs, c='red', alpha=0.5) #alpha controls a color’s transparency
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # facecolor determines the color of the shaded region 
    # Format plot.
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA" 
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16) 
    fig.autofmt_xdate() # draws the date labels diagonally to prevent them from overlapping
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
 












