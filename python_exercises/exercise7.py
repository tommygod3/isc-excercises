print("---------- Exercise 7 script ----------")

print("Question 1:")
a = list(range(3))
b = a
print(f"a: {a}, b: {b}")
b[0] = "hello"
print(f"a: {a}, b: {b}")
a.append(3)
print(f"a: {a}, b: {b}")

print("Question 2:")
a = "can I change"
b = a
print(f"a: {a}, b: {b}")
b = "different"
print(f"a: {a}, b: {b}")

print("Question 3:")
a = [1, 2, 3]
import copy
b = copy.deepcopy(a)
print(f"a: {a}, b: {b}")
b[0] = "hello"
print(f"a: {a}, b: {b}")
