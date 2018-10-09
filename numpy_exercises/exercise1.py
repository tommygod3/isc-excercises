print("---------- Exercise 1 script ----------")

print("Question 1:")
import numpy as np
x = range(1, 11)
a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)
print(f"a1's type: {a1.dtype}")
print(f"a2's type: {a2.dtype}")

print("Question 2:")
arr0 = np.zeros((2, 3, 4))
arr1 = np.ones((2, 3, 4))
arr2 = np.arange(1000)

print("Question 3:")
a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print(f"a[1]: {a[1]}")
print(f"a[1:4]: {a[1:4]}")
a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],
[1, 22, 4, 0.1, 5.3, -9],
[3, 1, 2.1, 21, 1.1, -2]])
print(f"a[:, 3]: {a[:, 3]}")
print(f"a[1:4, 0:4]: {a[1:4, 0:4]}")
print(f"a[1:, 2]: {a[1:, 2]}")
