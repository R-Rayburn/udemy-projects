import numpy as np


my_list = [x * 10 for x in range(1, 11)]

my_array = np.array(my_list)

print(f'size: {my_array.size}') # 10
print(f'shape: {my_array.shape}') # (10,)
print(f'demensions: {my_array.ndim}') # 1
print(f'type: {my_array.dtype}') # int64