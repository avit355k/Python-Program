import numpy as np

arr = np.array([0, 2, 0, 4, 0, 6, 0, 8, 0])

count = np.count_nonzero(arr)

print("Number of non-zero elements:", count)
