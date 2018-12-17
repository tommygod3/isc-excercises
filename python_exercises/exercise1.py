print("---------- Exercise 1 script ----------")

print("Question 1:")
course = "python"
rating = 10
print(f"Course: {course}, rating: {rating}")

print("Question 2:")
b = 3
c = 4
a = ((b*b) + (c*c))**0.5
print(f"a = {a}")

print("Question 3:")
print(f"a's type: {type(a)}")
print(f"b's type: {type(b)}")
print(f"c's type: {type(c)}")

print("Question 4:")
a = int(a)
print(f"a's type: {type(a)}")
try:
    print(a + " squared equals " + b + " squared +" + c + " squared.")
except TypeError as err:
    print(f"Type Error! Error message:\n{err}")
print("Done properly:\n" + str(a) + " squared equals " + str(b) + " squared + " + str(c) + " squared.")
