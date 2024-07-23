import numpy as np


# EXERCISE 1
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


# RANDOM NUMBERS
rng = np.random.default_rng(12345)

# useful with sampling data by taking values over or under a margin (sample half by taking items in indexes that are greater than 0.5)
random_array = rng.random(10)
print(random_array)

mean, stddev = 5, 1 # center around 5, plots as normal distribution
random_normal = rng.normal(mean, stddev, size=10)
print(random_normal)

# create list size of 100 containing random integers between 1 and 100
print(rng.integers(1, 101, 100))


# EXERCISE 2
# Create array of 5r 2c containing 10 to 100 at multiples of 10
a = np.arange(10, 101, 10).reshape(5, 2)
# np.linspace(10, 100, 10).reshape(5, 2)
# (np.aragne(1, 11) * 10).reshape(5, 2)
print(a)

# Create array of ran num n where 1 > n > 0 in 3 x 3 matrix
rng = np.random.default_rng(2022)
a = rng.random(9).reshape(3,3)
print(a)