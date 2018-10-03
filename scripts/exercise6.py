print("---------- Exercise 6 script ----------")

print("Question 1:")
s = "I love to write Python"
for letter in s:
    print(letter, end=" ")
print(f"\n5th element: {s[4]}")
print(f"Last element: {s[-1]}")
print(f"Length: {len(s)}")
print(f"s[0]: {s[0]}")
print(f"s[0][0]: {s[0][0]}")
print(f"s[0][0][0]: {s[0][0][0]}")
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
print(f"dir(something):\n{dir(something)}")
print(f"t's in something: {something.count('t')}")
print(f"Position of 'plete': {something.find('plete')}")
print(f"Split across e: {something.split('e')}")
thing2 = something.replace("Different", "Silly")
print(thing2)
try:
    something[0] = "B"
except TypeError as err:
    print(f"TyperError! Error message:\n{err}")
