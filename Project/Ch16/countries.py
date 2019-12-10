# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341

#Obtaining Two-Digit Country Codes
from pygal_maps_world.i18n import COUNTRIES
#In the for loop we tell Python to sort the keys in alphabetical order 
for country_code in sorted(COUNTRIES.keys()):    
    print(country_code, COUNTRIES[country_code])

