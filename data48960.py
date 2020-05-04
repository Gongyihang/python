import random
import numpy as np

data = [np.random.permutation(48) for _ in range(1920)]
np.savetxt("data1920.txt", data, fmt="%d")

cities = np.random.rand(48, 2)
np.savetxt("cities.txt", cities)