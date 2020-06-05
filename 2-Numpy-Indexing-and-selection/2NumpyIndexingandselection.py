import numpy as np

#creating sample array
arr = np.arange(0,11)
#show
print(arr)

'''
Bracket Indexing and Selection
'''
print('--Bracket Indexing and Selection--')
#Get a value at an index
print(arr[8])
#Get values in a range
print(arr[1:5])
#Get values in a range
print(arr[0:5])

'''
Broadcasting
'''
print('--Broadcasting--')
#Setting a value with index range (Broadcasting)
arr[0:5]=100

#Show
print(arr)
# Reset array, we'll see why I had to reset in  a moment
arr = np.arange(0,11)
#Show
print(arr)

#Important notes on Slices
slice_of_arr = arr[0:6]
#Show slice
print(slice_of_arr)
#Change Slice
slice_of_arr[:]=99
#Show Slice again
print(slice_of_arr)
print(arr)
#To get a copy, need to be explicit
arr_copy = arr.copy()
print(arr_copy)

'''
Indexing a 2D array (matrices)
'''
print('--Indexing a 2D array (matrices)--')
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
#Show
print(arr_2d)
#Indexing row
print(arr_2d[1])
# Format is arr_2d[row][col] or arr_2d[row,col]
# Getting individual element value
arr_2d[1][0]
# Getting individual element value
arr_2d[1,0]
# 2D array slicing
#Shape (2,2) from top right corner
arr_2d[:2,1:]
#Shape bottom row
arr_2d[2]
#Shape bottom row
arr_2d[2,:]

'''
Fancy Indexing
'''
print('--Fancy Indexing--')
#Set up matrix
arr2d = np.zeros((10,10))
#Length of array
arr_length = arr2d.shape[1]
#Set up array
for i in range(arr_length):
    arr2d[i] = i
    
print(arr2d)

#Fancy indexing allows the following
print(arr2d[[2,4,6,8]])
#Allows in any order
print(arr2d[[6,4,2,7]])

'''
Selection
'''
print('--Selection--')
arr = np.arange(1,11)
print(arr)
print(arr > 4)
bool_arr = arr>4
print(bool_arr)
print(arr[bool_arr])
print(arr[arr>2])
x = 2
print(arr[arr>x])