print("---------- Exercise 3 script ----------")

print("Question 1:")
x = [1, 2, 3, 4, 5]
print(f"Second item: {x[1]}")
print(f"Second to last item: {x[-2]}")
print(f"Whole list sliced: {x[:]}")
print(f"Second to fourth items slice: {x[1:4]}")

print("Question 2:")
y = list(range(1,11))
y[0] = 10
y.append(11)
y.extend([12,13,14])
print(y)

print("Question 3:")
forward = []
backward = []
values = ["a", "b", "c"]
for item in values:
    forward.append(item)
    backward.insert(0, item)
print(f"Forward: {forward}\nBackward: {backward}")
forward.reverse()
print(f"Forward is the same as backward: {forward==backward}")

print("Question 4:")
countries = ["uk", "usa", "uk", "uae"]
print(f"dir(countries):\n{dir(countries)}")
help(countries.count)
counter = countries.count("uk")
print(f"uk appears {counter} times")
