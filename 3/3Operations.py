'''
Operations
'''

import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

'''
Info on Unique Values
'''
print('--Info on Unique Values--')
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

'''
Selecting Data
'''
print('--Selecting Data--')
#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)
'''
Applying functions
'''
print('--Applying Functions--')
def times2(x):
    return x*2
print(df['col1'].apply(times2))
print(df['col3'].apply(len))
print(df['col1'].sum())
#Permanently Removing a column
del df['col1']
print(df)
#get coloumn and index names
print(df.columns)
print(df.index)

#Sorting and Ordering a DataFrame
print(df)

df.sort_values(by='col2') #inplace=False by default
#if you want to change it, just add paramter inplace =  true

#Find Null Values or Check for Null Values
print(df.isnull())

#Drop rows with Nan Values
df.dropna()

#Filling NaN values with something
import numpy as np
#new dataframe
df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()

print(df.fillna('FILL'))

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))

