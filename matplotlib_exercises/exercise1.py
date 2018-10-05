print("---------- Exercise 1 script ----------")

print("Question 1:")
import matplotlib.pyplot as plt
plt.plot(range(10))
plt.show()

print("Question 2:")
times = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
plt.plot(times, co2)
plt.plot(times, co2, 'b--')
plt.title("Concentration of CO2 versus time")
plt.ylabel("[CO2]")
plt.xlabel("Time (decade)")
plt.show()

print("Question 3:")
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
plt.plot(times, co2, 'b--', times, temp, 'r*-')
plt.savefig("data/co2_temp.pdf")
plt.show()
