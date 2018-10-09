print("---------- Exercise 4 script ----------")

print("Question 1:")
import numpy.ma as MA
marr = MA.masked_array(range(10), fill_value = -999)
print(f"marr, marr.fill_value:\n{marr, marr.fill_value}")
marr[2] = MA.masked
print(f"marr:\n{marr}")
print(f"marr.mask:\n{marr.mask}")
narr = MA.masked_where(marr > 6, marr)
print(f"narr:\n{narr}")
x = MA.filled(narr)
print(f"x:\n{x}")
print(f"type(x):\n{type(x)}")

print("Question 2:")
import numpy as np
m1 = MA.masked_array(range(1, 9))
print(f"m1:\n{m1}")
m2 = m1.reshape(2, 4)
print(f"m2:\n{m2}")
m3 = MA.masked_greater(m2, 6)
print(f"m3:\n{m3}")
res = m3 - np.ones((2, 4))
print(f"res:\n{res}")
print(f"type(res):\n{type(res)}")
