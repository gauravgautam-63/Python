"""
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like
i for integers, u for unsigned integers etc.
Below is a list of all data types in NumPy and the characters used to represent them.
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)

# Creating Arrays With a Defined Data Type
import numpy as np

arr = np.array([1, 2, 3, 4], dtype="S")
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype="i4")
print(arr)
print(arr.dtype)

# Converting Data Type on Existing Arrays
"""
The best way to change the data type of an existing array, is to make a copy of 
the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the
data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for
integer etc. or you can use the data type directly like float for float and int for integer. 
"""

import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)