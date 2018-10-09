print("---------- Exercise 10 script ----------")

print("Question 1:")
a = set(range(6))
b = set(range(2,9,2))
print(f"a: {a}")
print(f"b: {b}")
print(f"a union b: {a.union(b)}")
print(f"a intersect b: {a.intersection(b)}")

print("Question 2:")
band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}
for member in band:
    if member in counts.keys():
        counts[member] += 1
    else:
        counts[member] = 1
for count in counts:
    print(f"Member: {count}, count: {counts[count]}")

print("Question 3:")
if {}: print("hi") # Will not print
d = {"maggie": "uk", "ronnie": "usa"}
print(f"dir(d):\n{dir(d)}")
print(f"d.items(): {d.items()}")
print(f"d.keys(): {d.keys()}")
print(f"d.values(): {d.values()}")
print(f"maggie: {d.get('maggie','Not found!')}") # If key not found, will print 'Not found!'
print(f"mikhail: {d.get('mikhail','Not found!')}")
print(f"mikhail: {d.setdefault('mikhail','ussr')}") # If mikhail not found, will add to dict with value ussr
