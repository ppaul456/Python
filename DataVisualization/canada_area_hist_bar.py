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

#clean the data set to remove a few unnecessary columns
# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))

#rename the columns so that they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

# let's examine the types of the column labels, change it to string(all column labels of type string)
all(isinstance(column, str) for column in df_can.columns)
df_can.columns = list(map(str, df_can.columns))
print(df_can.columns.values)

#setting the 'Country' column as the index using set_index() method
df_can.set_index('Country', inplace=True)

#add a 'Total' column that sums up the total immigrants by country over the entire period
df_can['Total'] = df_can.sum(axis=1) #axis = 0 means along the column and axis = 1 means working along the row.
print ('data dimensions:', df_can.shape)  # 38 cloumns now

# finally, let's create a list of years from 1980 - 2013
years = list(map(str, range(1980, 2014)))
print(years)

########################################################################
## Visualization Data
import matplotlib as mpl
import matplotlib.pyplot as plt
print ('Matplotlib version: ', mpl.__version__) #Matplotlib version

## Area Plots
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True) #axis = 0 means along the column
# get the top 5 entries
df_top5 = df_can.head()
print(df_top5.head())
# transpose the dataframe
df_top5 = df_top5[years].transpose() 
print(df_top5.head())

#Area plots are stacked by default, to produce an unstacked plot, pass stacked=False.
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='area', 
             stacked=False,
             alpha=0.25, # 0-1, default value a= 0.5, transparency (alpha value) can modify by passing in the alpha
             figsize=(20, 10), # pass a tuple (x, y) size
             )
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

# option 2: preferred option with more flexibility
ax = df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10))
ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')

########################################################################
## Numpy's Histograms
# let's quickly view the 2013 data
print(df_can['2013'].head())

#By default, the histrogram method breaks up the dataset into 10 bins. 
# summarizes the bin ranges and the frequency distribution of immigration in 2013
# np.histogram returns 2 values
count, bin_edges = np.histogram(df_can['2013'])
print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins
#178 countries contributed between 0 to 3412.9 immigrants
#11 countries contributed between 3412.9 to 6825.8 immigrants
#1 country contributed between 6285.8 to 10238.7 immigrants

# Wrong Histogram
df_can['2013'].plot(kind='hist', figsize=(8, 5)) #the x-axis labels do not match with the bin size
plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label
#plt.show()

# Correct Histogram
# 'bin_edges' is a list of bin intervals
count, bin_edges = np.histogram(df_can['2013'])
df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)  # xticks= x 刻度
plt.title('Histogram of Immigration from 195 countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label
plt.show()

##What is the immigration distribution for Denmark, Norway, and Sweden for years 1980 - 2013?
# let's quickly view the dataset 
df_s = df_can.loc[['Denmark', 'Norway', 'Sweden'], years]
print(df_s.head())
# transpose dataframe
df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose() # 交換rows and columns
print(df_t.head())
# Generate Histogram
# let's get the x-tick values
count, bin_edges = np.histogram(df_t, 15)
# un-stacked histogram
df_t.plot(kind ='hist', 
          figsize=(10, 6),
          bins=15,
          alpha=0.6,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen']
         )
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()

#######################################################################
## Bar Charts 
# kind=bar creates a vertical bar plot
# kind=barh creates a horizontal bar plot

# step 1: get the data
df_iceland = df_can.loc['Iceland', years]
print(df_iceland.head())

# step 2: plot data
df_iceland.plot(kind='bar', figsize=(10, 6), rot=90) # rotate the bars by 90 degrees

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')
# Annotate arrow
plt.annotate('',                      # s: str. Will leave it blank for no text
             xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',         # will use the coordinate system of the object being annotated 
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )
# Annotate Text
# rotation: rotation angle of text in degrees (counter clockwise)
# va: vertical alignment of text [‘center’ | ‘top’ | ‘bottom’ | ‘baseline’]
# ha: horizontal alignment of text [‘center’ | ‘right’ | ‘left’]
plt.annotate('2008 - 2011 Financial Crisis', # text to display
             xy=(28, 30),                    # start the text at at point (year 2008 , pop 30)
             rotation=72.5,                  # based on trial and error to match the arrow
             va='bottom',                    # want the text to be vertically 'bottom' aligned
             ha='left',                      # want the text to be horizontally 'left' algned.
            )
plt.show()