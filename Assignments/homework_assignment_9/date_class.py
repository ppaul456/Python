#Pohsun Chang
#830911
#MSITM6341
#11/24/2019

class Date():             # create a class

    def __init__(self):         # special function in python __init__, self (key word in python) is the object that prestents
        self.day = ""
        self.month = ""
        self.year = ""
        self.date ={}          # set change_date as a dic  

    def print_date(self):         # self(special key) need to be first
        print(self.month + " " + str(self.day)+ "," + " " + str(self.year))  # call the properties from class, convert int to str

    def change_date(self):   # self need to be written     
        self.date["day"] = self.day       # save all Data()'s properties into date dic 
        self.date["month"] = self.month
        self.date["year"] = self.year

my_date = Date()

my_date.day = 12
my_date.month = "June"
my_date.year = 2019

my_date.print_date()       # call print_date function

my_date.change_date()      # call change_date function
print(my_date.date)

