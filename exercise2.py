print("---------- Exercise 2 script ----------")

print("Question 1:")
print("""while True:
    print("Infinity")""")
print("Escape with Ctrl-C")
number = 10
while number > 100:
    print("Not going to get executed")

print("Question 2:")
gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0
while count < 4:
    item = gases[count]
    print(f"Gas: {item}, index: {count}")
    count+=1

print("Question 3:")
name = "Lisa"
if name == "Lisa":
    print(f"{name} plays saxaphone")
elif name == "Bart":
    print(f"{name} rides skateboard")
else:
    print(f"{name} lives in Springfield")

print("Question 4:")
x = 1
if x:
    print(f"{x} is True")
number = 22.1
if number:
    print(f"{number} is True")
word = "hello"
if word:
    print(f"\"{word}\" is True")
array = [1,2]
if array:
    print(f"{array} is True")
zero_int = 0
if zero_int:
    print(f"{zero_int} is True")
else:
    print(f"{zero_int} is False")
zero_float = 0.0
if zero_float:
    print(f"{zero_float} is True")
else:
    print(f"{zero_float} is False")
