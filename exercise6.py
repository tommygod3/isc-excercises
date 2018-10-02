print("---------- Exercise 6 script ----------")

print("Question 1:")
s = "I love to write Python"
for letter in s:
    print(letter, end=" ")
print(f"\n5th element: {s[4]}")
print(f"Last element: {s[-1]}")
print(f"Length: {len(s)}")
print(s[0])
print(s[0][0])
print(s[0][0][0])
# s[0] is first element
# s[0][0] is s[0]'s first element
# and so on

print("Question 2:")
s = "I love to write Python"
split_s = s.split()
for word in split_s:
    if word.lower().find("i") > -1:
        print(f"I found 'i' in {word}")

print("Question 3:")
something = "Completely Different"
print(dir(something))
print(something.count("t"))
print(something.find("plete"))
print(something.split("e"))
thing2 = something.replace("Different", "Silly")
print(thing2)
try:
    something[0] = "B"
except TypeError as err:
    print(f"TyperError! Error message:\n{err}")
