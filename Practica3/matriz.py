# Imports
import matplotlib.pyplot as plt
import numpy as np

# Definimos la matriz para la practica 3
array = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,1,0,0,0,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]).reshape(9, 15)

plt.imshow(array, cmap="gray")
plt.show()