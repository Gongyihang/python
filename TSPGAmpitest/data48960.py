import random
import numpy as np

data = [np.random.permutation(48) for _ in range(60)]
np.savetxt("data60.txt", data, fmt="%d")

# cities = np.random.rand(48, 2)
# np.savetxt("cities.txt", cities)