import numpy as np


# EXERCISE 1
age_list = [22, 34, 57, 65, 87, 19, 44]

age_array = np.array(age_list)

size = age_array.size
shape = age_array.shape

print(size)  # 7
print(shape)  # (7,)


# EXERCISE 2
my_list = [x * 10 for x in range(1, 11)]

my_array = np.array(my_list)

print(f'size: {my_array.size}') # 10
print(f'shape: {my_array.shape}') # (10,)
print(f'demensions: {my_array.ndim}') # 1
print(f'type: {my_array.dtype}') # int64