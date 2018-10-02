print("---------- Exercise 4 script ----------")

print("Question 1:")
t = (1,)
print(t[-1])
tup = tuple(range(100,201))
print(tup[0], tup[-1])

print("Question 2:")
mylist = [23, "hi", 2.4e-10]
for (count, item) in enumerate(mylist):
    print(count, item)

print("Question 3:")
(first, middle, last) = mylist
print(first,middle,last)
(first, middle, last) = (middle, last, first)
print(first,middle,last)
