## Regression Plots
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')

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

# create a list of years from 1980 - 2013
years = list(map(str, range(1980, 2014)))
print(years)

# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']
# view the final dataframe
print(df_tot.head())

## With seaborn, generating a regression plot is calling the regplot function.
# Customize the color and marker of the scatter plot and regression line
plt.figure(figsize=(15, 10))
sns.set(font_scale=1.5)
sns.set_style('ticks') # change background to white background
#sns.set_style('whitegrid') # a white background with gridlines
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')

plt.show()