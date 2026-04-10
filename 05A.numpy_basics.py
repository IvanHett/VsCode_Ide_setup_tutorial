# =========================
# NUMPY BASICS TUTORIAL
# =========================

# 1. IMPORT NUMPY
import numpy as np

print("______________________________1. Creating Arrays______________________________")

# 2. CREATE ARRAYS
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print("Array 1:", arr1)
print("Array 2:", arr2)


print("\n______________________________2. Basic Operations__________________________________")

# 3. ARRAY OPERATIONS
print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)


print("\n______________________________3. Indexing__________________________________")

# 4. INDEXING
print("First element:", arr1[0])
print("Last element:", arr1[-1])


print("\n______________________________4. Useful Functions__________________________________")

# 5. USEFUL FUNCTIONS
print("Mean:", np.mean(arr1))
print("Sum:", np.sum(arr1))
print("Max:", np.max(arr1))


print("\n______________________________5. Multi-Dimensional Arrays__________________________________")

# 6. 2D ARRAY
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Matrix:\n", matrix)
print("Shape:", matrix.shape)


print("\n______________________________6. Real Example__________________________________")

# 7. REAL USE CASE
prices = np.array([10, 20, 30])
quantity = np.array([2, 1, 3])

total = prices * quantity

print("Total per item:", total)
print("Final total:", np.sum(total))