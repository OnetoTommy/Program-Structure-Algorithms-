import numpy as np

# Creating a 1D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape 1D array to 2D array (4 rows, 3 columns)
newarr2D = arr.reshape(4, 3)
print("2D Array (4x3):")
print(newarr2D)

# Reshape 1D array to 3D array (2 blocks, 3 rows, 2 columns)
newarr3D = arr.reshape(2, 3, 2)
print("\n3D Array (2x3x2):")
print(newarr3D)