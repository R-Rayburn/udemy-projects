import numpy as np

age_list = [22, 34, 57, 65, 87, 19, 44]

age_array = np.array(age_list)

size = age_array.size
shape = age_array.shape

print(size)  # 7
print(shape)  # (7,)