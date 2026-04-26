import numpy as np

# Arrays
# Array = collection of values.
# ==============================================================================================
# Python list: #
# numbers = [1, 2, 3, 4]

# Numpy Arrays #
numbers = np.array([1,2,3,4])
# print(numbers)
# ==============================================================================================

# Python List #
a=[1,2,3,4]
b=[1,2,3,4]
# print(a+b)  => Output =>[1, 2, 3, 4, 1, 2, 3, 4]

# Numpy arrays addition #
first = np.array([1,2,3,4])
second = np.array([1,2,3,4])
# print(first+second) => Output => [2 4 6 8]

# ==============================================================================================
# 1. Normal array
arr1 = np.array([10, 20, 30])

# 2. Zero array
arr2 = np.zeros(5)
# print(arr2) => Output => [0. 0. 0. 0. 0.]

# 3. Ones array
arr3= np.ones(10) 
# print(arr3) => Output => [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# 4. Range array
arr4 = np.arange(1,10)
# print(arr4) => Output => [1 2 3 4 5 6 7 8 9]

# Array properties
arr = np.array([1,2,3,4])
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr[0]) => First Value
# print(arr[-1]) => Last Value

# Array Slicing
# Syntax => arr[start:end]
arraySlicing = np.array([1,2,3,4,5,6,7,8,9])
# print(arraySlicing[2:4])


# print(arraySlicing.mean())
# print(arraySlicing.min())
# print(arraySlicing.max())

