import numpy as np

# np.ones((rows, cols), dtype)
print(np.ones(4,)) # same as array([1., 1., 1., 1.])

# np.zeros((rows, cols) dtype)
print(np.zeros((2,5), dtype=int))

# np.arrange(start, stop, step)
#  stop not inclusive
print(np.arange(10))

# np.linspace(start, stop, n) <- n=number of elements in array
#  equally spaces values
#  stop is inclusive
print(np.linspace(0, 100, 5))
print(np.linspace(0, 5, 20))

# reshape(rows, cols)
#  area must equal len of array
print(np.arange(1, 9, 2).reshape(4, 1))