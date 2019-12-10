# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341

import json
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle  
# Load the data into a list. 
# Converting Strings into Numerical Values
# Plotting a Complete Population Map
# Grouping Countries by Population
# Styling World Maps in Pygal  
filename = 'population_data.json' 
with open(filename) as f:  
    pop_data = json.load(f)
    
    # Build a dictionary of population data. 
    cc_populations = {} 
    for pop_dict in pop_data:      
        if pop_dict['Year'] == '2010':      # Each item is a dictionary with four key-value pairs, and store each dictionary in pop_dict
            country_name = pop_dict['Country Name']        
            population = int(float(pop_dict['Value'])) #The float() function turns the string into a decimal, int() function drops the decimal part    
            # print(country_name + ": " + str(population))
            code = get_country_code(country_name)  # call get_country_code() function      
            if code:     
            #     print(code + ": "+ str(population)) # code returns
            # else:            
            #     print('ERROR - ' + country_name)    # code not returns
                cc_populations[code] = population
    # Group the countries into 3 population levels. 
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}  
    for cc, pop in cc_populations.items():    
        if pop < 10000000:        
            cc_pops_1[cc] = pop    
        elif pop < 1000000000:        
            cc_pops_2[cc] = pop    
        else:        
            cc_pops_3[cc] = pop
    # See how many countries are in each level.        
    print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


wm = pygal.maps.world.World() 
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle) 
wm = pygal.maps.world.World(style=wm_style) 
# Pygal’s styling directives to rectify the colors
wm.title = 'World Population in 2010, by Country' 
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1) 
wm.add('10m-1bn', cc_pops_2) 
wm.add('>1bn', cc_pops_3)  

wm.render_to_file('world_population.svg')






