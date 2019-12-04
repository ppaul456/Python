# Name:Pohsun Chang
# Student ID: 830911
# Due Date:  12/03/2019
# MSITM 6341

class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0

    def print_dimensions(self):
        print("Dimensions of rectangle: " + str(self.width) +"*"+ str(self.height))

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = self.width*2 + self.height*2
        return perimeter


my_rectangle = Rectangle()

my_rectangle.width = 4
my_rectangle.height = 5

my_rectangle.print_dimensions()
print(my_rectangle.get_area())
print(my_rectangle.get_perimeter())


