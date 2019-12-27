#The first thing we'll do is import two key data analysis modules: pandas and Numpy.
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
#Install module is xlrd,which pandas requires to read in excel files.

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')

print (df_can.head())
# view top 5,tip: You can specify the number of rows you'd like to see
print (df_can.tail())
# view last 5


print(df_can.columns.values) #To get the list of column headers we can call upon the dataframe's .columns parameter.
print(df_can.index.values) #To get the list of indicies we use the `.index` parameter.
print(df_can.info()) #Getting basic information about your dataframe

#clean the data set to remove a few unnecessary columns
# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))

#rename the columns so that they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

#add a 'Total' column that sums up the total immigrants by country over the entire period,axis=1 represents columns 
df_can['Total'] = df_can.sum(axis=1)
#view a quick summary of each column in our dataframe using the describe() method
print(df_can.describe())

#filtering on the list of countries ('Country')
df_can.Country  # returns a series
#filtering on the list of countries ('OdName') and the data for years: 1980 - 1985.
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]) # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.

#setting the 'Country' column as the index using set_index() method
df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
print(df_can.head(3))
# optional: to remove the name of the index
df_can.index.name = None

#view the number of immigrants from Japan (row 87) for the following scenarios: 
# 1. The full row data (all columns) 
# 2. For year 2013 
# 3. For years 1980 to 1985

# 1. the full row data (all columns)
print(df_can.loc['Japan'])
# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
print(df_can.loc['Japan', 2013])
# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

df_can.columns = list(map(str, df_can.columns))
print ((type (x)) for x in df_can.columns.values) #<-- uncomment to check type of column headers

# useful for plotting later on
years = list(map(str, range(1980, 2014)))   #第一个参数 function(str) 以第二参数中的元素调用 function 函数，還傳新的列表['1980'...'2014']
print(years)

#filter the dataframe to show the data on Asian countries (AreaName = Asia)
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

# 2. pass this condition into the dataFrame
print(df_can[condition])
# we can pass mutliple criteria in the same line. 
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

import matplotlib as mpl
import matplotlib.pyplot as plt

#Line Pots 
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())

#plot a line plot by appending .plot() to the haiti dataframe.
haiti.plot()

# label the x and y axis using plt.title(), plt.ylabel(), and plt.xlabel() as follows:
haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure

#Haiti spiked up from 2010 as Canada stepped up its efforts to accept refugees from Haiti.
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below
#The x-axis (years) is type 'integer', we specified x as a year. 
#The y axis (number of immigrants) is type 'integer', so we can just specify the value y = 6000.
plt.show() 
