import numpy as np
import pandas as pd

array_1 = np.array([10, 20, 3])

#print (type(array_1))

# N dimensional arrays
array_2 = np.array([[1, 2, 3], [4, 5, 6]])
#print(array_2)

#Array with many elements
array_3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]], [[13,14,15,16], [17,18,19,20], [21,22,23,24]]])
#print(array_3)

# Gete shape of array_2 and array_3
# print(array_2.shape)  # Output: (2, 3)
# print(array_3.shape)  # Output: (3, 4)

# Get the number of dimensions
# print(array_1.ndim)  # Output: 1
# print(array_2.ndim)  # Output: 2
# print(array_3.ndim)  # Output: 3

# get size of array_1, array_2 and array_3
# print(array_1.size)  # Output: 3
# print(array_2.size)  # Output: 6
# print(array_3.size)  # Output: 24

df1 = pd.DataFrame(array_1)
df2 = pd.DataFrame(array_2)
df3 = pd.DataFrame(array_3.reshape(4,6))

# print(df1)
# print(df2)
# print(df3)

ar_zeros = np.zeros(5)
# print(ar_zeros)  # Output: [0. 0. 0. 0. 0.]

ar_ones = np.ones(5)
# print(ar_ones)  # Output: [1. 1. 1. 1. 1.]

# np.arange([start,] stop[, step], dtype=None)
our_array = np.arange(1, 20, 4)
# print(our_array)  # Output: [ 1  5  9 13 17]

# Random numbers
random_array_1 = np.random.randint(10, 30, size=(4,7))
#print(random_array_1)  # Output: Random numbers in a 10x30 array

random_array_2 = np.random.rand(4, 7)
#print(random_array_2)  # Output: Random numbers in a 4x7 array with values between 0 and 1

np.random.seed(0)
random_array_3 = np.random.randint(10, 30, size=(4,7))
print(random_array_3)  # Output: Random numbers in a 4x7 array with values between 0 and 1, reproducible with seed

random_array_6 = np.random.randint(2, 100, size=(3, 4, 5, 6))
print(random_array_6)  # Output: Random numbers in a 3x4x5x6 array with values between 2 and 100



