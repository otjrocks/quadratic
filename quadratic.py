'''
Quadratic Formula Calculator
By: Owen Jennings

parent function:
y = ax**2 + bx + c
Formulas:
-b +- (square root b**2 - 4ac) / 2a
'''

import math

# input values
a = float(input("\n\n\na term: "))
b = float(input("b term: "))
c = float(input("c term: "))


discriminate = b**2 - 4*(a)*(c)
if discriminate < 0:
    print("\n\n\nNo Solutions!")
elif discriminate == 0:
    print("\n\nOnly One Solution!")
    ans =  (-(b) + (math.sqrt(b**2 - 4*(a)*(c)))) / (2 * a)
    print("Solution: " + str(ans))
else:
    ans =  (-(b) + (math.sqrt(b**2 - 4*(a)*(c)))) / (2 * a)
    ans2 =  (-(b) - (math.sqrt(b**2 - 4*(a)*(c)))) / (2 * a)
    print("\nEquation: " + str(-1 * b) + " +/- √(" + str(b**2 - 4*(a)*(c)) + ") / " + str(2 / a))
    print("Discriminate: " + str(discriminate))
    print("\n\nAnswer rounded to the fourth digit: ")
    print("Solution 1: " + str(round(ans, 4)) + "\nSolution 2: " + str(round(ans2, 4)))

# check if the square root is a float or integer and decide whether to display whole number or square root equation
