print("---------- Exercise 8 script ----------")

print("Question 1:")
def double_it(number):
    return number * 2
print(f"double_it(2): {double_it(2)}")
print(f"double_it(2.0): {double_it(2.0)}")
print(f"double_it(two): {double_it('two')}")

print("Question 2:")
import math
def calc_hypo(a, b):
    hypo = math.sqrt((a * a) + (b * b))
    return hypo
print(f"calc_hypo(3,4): {calc_hypo(3,4)}")

print("Question 3:")
def calc_hypo(a, b):
    if type(a) != int and type(a) != float:
        print("Bad argument")
        return False
    if type(b) != int and type(b) != float:
        print("Bad argument")
        return False
    if a <= 0 or b <= 0:
        print("Bad argument")
        return False
    hypo = math.sqrt((a * a) + (b * b))
    return hypo

print(f"calc_hypo('a',2): {calc_hypo('a',2)}")
print(f"calc_hypo(2,'b'): {calc_hypo(2,'b')}")
print(f"calc_hypo('a','b'): {calc_hypo('a','b')}")
print(f"calc_hypo(-1,2): {calc_hypo(-1,2)}")
print(f"calc_hypo(2,-1): {calc_hypo(2,-1)}")
print(f"calc_hypo(-1,-1): {calc_hypo(-1,-1)}")
print(f"calc_hypo(2,2): {calc_hypo(2,2)}")
