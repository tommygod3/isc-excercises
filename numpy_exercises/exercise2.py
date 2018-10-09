print("---------- Exercise 2 script ----------")

print("Question 1:")
import numpy as np
arr = np.array([range(4), range(10, 14)])
print(f"arr.shape: {arr.shape}")
print(f"arr.size: {arr.size}")
print(f"arr.max(): {arr.max()}")
print(f"arr.min(): {arr.min()}")

print("Question 2:")
print(f"np.reshape(arr, (2, 2, 2)):\n{np.reshape(arr, (2, 2, 2))}")
print(f"np.transpose(arr):\n{np.transpose(arr)}")
print(f"np.ravel(arr):\n{np.ravel(arr)}")
print(f"arr.astype(np.float64):\n{arr.astype(np.float64)}")
