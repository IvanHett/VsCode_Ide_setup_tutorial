#open new terminal and type pip install matplotlib
import matplotlib as plt
import numpy as np

#checking version
print(plt.__version__)

#plotting 
import matplotlib.pyplot as plt
xpoints = np.array([1,8])
ypoints = np.array([2,5])

plt.plot(xpoints,ypoints)
plt.show()

