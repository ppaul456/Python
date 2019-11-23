#Pohsun Chang
#830911
#MSITM6341
#11/24/2019

class Date():             # create a class

    def __init__(self):         # special function in python __init__, self (key word in python) is the object that prestents
        self.day = ""
        self.month = ""
        self.year = ""              

    def print_date(self):         # self(special key) need to be first
        print(self.month + " " + str(self.day)+ "," + " " + str(self.year))  # call the properties from class, convert int to str

    def change_date(self,day,month,year):   # self need to be written, and three properties     
        self.day = day                      
        self.month = month
        self.year = year

my_date = Date()
# assign properties for the Class
my_date.day = 12
my_date.month = "June"
my_date.year = 2019

my_date.print_date()       # call print_date function

my_date.change_date(14,"July",2020)   # call change_date function, assign new properties for the Class
my_date.print_date()

