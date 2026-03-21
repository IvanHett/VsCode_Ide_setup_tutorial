# ================================
# IMPORT LIBRARIES
# ================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ================================
# NUMPY (numbers / arrays)
# ================================
numbers = np.array([1, 2, 3, 4])
result = numbers * 2

print("NumPy result:", result)


# ================================
# PANDAS (table / data)
# ================================
data = {
    "Name": ["Ivan", "Alex"],
    "Age": [21, 22]
}

df = pd.DataFrame(data)

print("\nPandas Data:")
print(df)


# ================================
# MATPLOTLIB (graph)
# ================================
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Graph")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()

print("graph generated")