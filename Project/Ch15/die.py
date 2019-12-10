# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341


from random import randint
#Creating the Die Class
class Die():    
    """A class representing a single die."""  
    def __init__(self, num_sides=6):        
        """Assume a six-sided die."""        
        self.num_sides = num_sides            
        
    def roll(self):        
        """"Return a random value between 1 and number of sides."""       
        return randint(1, self.num_sides)  #This function(randint()) can return the starting value (1), the ending value (num_sides), or any integer between the two
        
