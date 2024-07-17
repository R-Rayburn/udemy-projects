import numpy as np


rng = np.random.default_rng(12345)

# useful with sampling data by taking values over or under a margin (sample half by taking items in indexes that are greater than 0.5)
random_array = rng.random(10)
print(random_array)


mean, stddev = 5, 1 # center around 5, plots as normal distribution
random_normal = rng.normal(mean, stddev, size=10)
print(random_normal)

# create list size of 100 containing random integers between 1 and 100
print(rng.integers(1, 101, 100))