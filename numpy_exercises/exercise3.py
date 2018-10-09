print("---------- Exercise 3 script ----------")

print("Question 1:")
import numpy as np
a = np.array([range(4), range(10, 14)])
b = np.array([2, -1, 1, 0])
print(f"a * b:\n{a * b}")
b1 = b * 100
b2 = b * 100.0
print(f"b1, b2:\n{b1, b2}")
print(f"b1 == b2:\n{b1 == b2}")
print(f"b1.dtype, b2.dtype:\n{b1.dtype, b2.dtype}")

print("Question 2:")
arr = np.arange(10)
print(f"arr < 3:\n{arr < 3}")
print(f"np.less(arr, 3):\n{np.less(arr, 3)}")
condition = np.logical_or(arr < 3, arr > 8)
new_arr = np.where(condition, arr * 5, arr * -5)
print(f"new_arr:\n{new_arr}")

print("Question 3:")
def calcMagnitude(u, v, minmag = 0.1): 
    mag = ((u**2) + (v**2))**0.5
    output = np.where(mag > minmag, mag, minmag)
    return output

u = np.array([[4, 5, 6], [2, 3, 4]])
v = np.array([[2, 2, 2], [1, 1, 1]])
print(f"calcMagnitude(u, v):\n{calcMagnitude(u, v)}")
u = np.array([[4, 5, 0.01], [2, 3, 4]])
v = np.array([[2, 2, 0.03], [1, 1, 1]])
print(f"calcMagnitude(u, v):\n{calcMagnitude(u, v)}")
