# =========================
# NUMPY ADVANCED
# =========================

import numpy as np

print("__________1. Reshape__________")

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print(reshaped)


print("\n__________2. Random Data__________")

random_arr = np.random.rand(5)

print(random_arr)


print("\n__________3. Filtering__________")

arr2 = np.array([10, 20, 30, 40])

print(arr2 > 20)
print(arr2[arr2 > 20])