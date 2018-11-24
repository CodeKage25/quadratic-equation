from math import *

a = float(input("please enter a number: "))
b = float(input("please enter a number: "))
c = float(input("please enter a number: "))

positive = (-b + sqrt(b**b-4*a*c))
negative = (-b - sqrt(b**b-4*a*c))

result = (positive/2*a, negative/2*a)
print(result)

