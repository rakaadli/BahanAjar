import numpy as np
import matplotlib.pyplot as plt

'''
Numpy Arrays
'''

my_list = [1,2,3]
#normal python List
print(my_list)
#With numpy List
print(np.array(my_list))

#normal python Matrix List
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
#With numpy List
print(np.array(my_matrix))

'''
Built in Methods
'''

'''
Arrange
'''

print(np.arange(0,10))

print(np.arange(0,11,2))

'''
Zero and ones
'''
print('--Zero and ones--')
print(np.zeros(3))
print(np.zeros((5,5)))
print(np.ones(3))
print(np.ones((3,3)))

'''
Linespace
'''
print('--Linespace--')
np.linspace(0,10,3)
np.linspace(0,10,50)

'''
Eye
'''
print(np.eye(4))

'''
Random 
'''

'''
rand
Create an array of the given shape and populate it with
random samples from a uniform distribution
over ``[0, 1)``.
'''
print(np.random.rand(2))
print(np.random.rand(5,5))
#uniform = np.random.rand(1000)
#pdf, bins, patches = plt.hist(uniform, bins=20, range=(0, 1), density=True)
#plt.title('rand: uniform')
#plt.show()

'''
randn
Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:
'''
print(np.random.randn(2))
print(np.random.randn(5,5))
normal = np.random.randn(1000)
#pdf, bins, patches = plt.hist(normal, bins=20, range=(-4, 4), density=True)
#plt.title('randn: Normal')
#plt.show()

'''
randint
Return random integers from low (inclusive) to high (exclusive).

'''
print(np.random.randint(1,100))
print(np.random.randint(1,100,10))

'''
Array Attributes Methods
'''
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr)
print(ranarr)

'''
Reshape
'''
arr.reshape(5,5)
print(arr)

'''
Min,Max,argmax,argmin
'''
print('--Min,Max,argmax,argmin--')
print(ranarr)
print(ranarr.max())
print(ranarr.argmax())
print(ranarr.min())
print(ranarr.argmin())

'''
Shape
'''
print('--Shape--')
print(arr.shape)
print(arr.reshape(1,25))
print(arr.reshape(1,25).shape)
print(arr.reshape(25,1))
print(arr.reshape(25,1).shape)

'''
dtype
'''
print('--dtype--')
print(arr.dtype)