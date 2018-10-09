print("---------- Exercise 5 script ----------")

print("Question 1:")
with open("data/weather.csv", "r") as reader:
    data = reader.read()
print("reader.read():")
print(data)

print("Question 2:")
print("reader.readline():")
with open("data/weather.csv", "r") as reader:
    line = reader.readline()
    while line:
        print(line)
        line = reader.readline()
print("It's over")

print("Question 3:")
with open("data/weather.csv", "r") as reader:
    header = reader.readline() # We will ignore this line
    rain = []
    for line in reader.readlines():
        r = line.strip().split(",")[-1]
        r = float(r)
        rain.append(r)
print(f"Last columns: {rain}")
with open("data/myrain.txt", "w") as writer:
    for r in rain:
        writer.write(str(r) + "\n")

print("Question 4:")
import struct
bin_data = struct.pack("bbbb", 123, 12, 45, 34)
with open("data/mybinary.dat", "wb") as bwriter:
    bwriter.write(bin_data)
with open("data/mybinary.dat", "rb") as breader:
    bin_data2 = breader.read()
data = struct.unpack("bbbb", bin_data2)
print(f"Binary data: {data}")
