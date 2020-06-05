# Introduction to Pandas

#In this section of the course we will learn how to use pandas for data analysis. You can think of pandas as an extremely powerful version of Excel, with a lot more features. In this section of the course, you should go through the notebooks in this order:

#* Introduction to Pandas
#* Series
#* DataFrames
#* Missing Data
#* GroupBy
# Merging,Joining,and Concatenating
# Operations
# Data Input and Output

import numpy as np
import pandas as pd

'''
### Creating a Series

You can convert a list,numpy array, or dictionary to a Series:
'''


labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

#using lists
print('using Lists')
print(pd.Series(data=my_list))
print(pd.Series(data=my_list,index=labels))
print(pd.Series(my_list,labels))

#using NumPy Arrays
print('using Numpy Arrays')
print(pd.Series(arr))
print(pd.Series(arr,labels))

#using dictionary
print('using Dictionary')
print(pd.Series(d))

'''
Data in a series
'''
#A pandas series can hold avariety of object types:
print(pd.Series(data=labels))
# Even functions (although unlikely that you will use this)
print(pd.Series([sum,print,len]))

'''
Using an Index
The key to using a Series is understanding its index. Pandas makes use of these index names or numbers by allowing for fast look ups of information (works like a hash table or dictionary).

Let's see some examples of how to grab information from a Series. Let us create two sereis, ser1 and ser2:
'''
print('--Using an Index--')
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan']) 
print(ser1)
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])      
print(ser2)          
ser1['USA']                 
#Operations are then also done based off of index:
print(ser1 + ser2)

print("-------------------DATAFRAMES-------------------")
'''
DataFrames are the workhorse of pandas and are directly inspired by the R programming language. We can think of a DataFrame as a bunch of Series objects put together to share the same index. Let's use pandas to explore this topic!
'''
import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
'''
Selection and indexing
'''
print('--Selection and indexing--')
df['W']
# Pass a list of column names
df[['W','Z']]
# SQL Syntax (NOT RECOMMENDED!)
df.W
#DataFrame Columns are just Series
print(type(df['W']))
#Creating a new coloumn
df['new'] = df['W'] + df['Y']
print(df)
#Remove Coloumn
df.drop('new',axis=1)
# Not inplace unless specified!
print(df)
df.drop('new',axis=1,inplace=True)
print(df)
#can also drop rows this way
print(df.drop('E',axis=0))
print(df.loc['A'])
print(df.iloc[2])
#memilih baris dan kolom
print(df.loc['B','Y'])
print(df.loc[['A','B'],['W','Y']])

'''
Conditional selection
'''
print('--Conditional Selection--')
print(df)
#cara menampilkan boolean
print(df>0)

#Cara mengisi data frame yang lebih dari 0 denga NaN
print(df[df>0])

# + ambil kolom Y
df[df['W']>0]['Y']

# + ambil kolom Y dan X
df[df['W']>0][['Y','X']]

#Ambil Baris  dengan 2 kondisi
df[(df['W']>0) & (df['Y'] > 1)]

'''
More Index Details
'''
print('--More Index Details--')
# Reset to default 0,1...n index
df.reset_index()
# buat data baru
newind = 'CA NY WY OR CO'.split()
df['States'] = newind
print(df)

'''
Multi Index and index hierarchy
'''
print('--Multi-Index and Index Hierarchy--')
# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)
#
print(df.loc['G1'])
print(df.loc['G1'].loc[1])
print(df.index.names)
df.index.names = ['Group','Num']
print(df)
print(df.xs('G1'))
print(df.xs(['G1',1]))
print(df.xs(1,level='Num'))