print("---------- Exercise 11 script ----------")

print("Question 1:")
from band import Band

print("Question 2:")
ws = Band("The White Stripes")
ws.employ("Meg", 100)
ws.employ("Jack", 100)
ws.write_annual_report()

print("Question 3:")
hs = Band("Hearsay")
members = ["Suzanne", "Danny", "Kym", "Myleene", "Noel"]
print(f"members: {members}")
for member in members:
    hs.employ(member, 10)
hs.write_annual_report()
hs.sack("Danny")
print("Danny has not been performing...")
print(f"Members: {hs.get_members()}")
print("Trying to employ Madonna: ")
hs.employ("Madonna", 1000000)
