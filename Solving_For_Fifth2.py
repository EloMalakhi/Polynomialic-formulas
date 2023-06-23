import sympy
import random
a,b,c,d,e,x = sympy.symbols('a b c d e x')
result = (sympy.expand((x-a)*(x-b)*(x-c)*(x-d)*(x-e)))



# mechanics
lvl1 = -a - b - c - d - e
lvl2 = a*b + a*c + a*d + a*e + b*c + b*d + b*e + c*d + c*e + d*e
lvl3 = -a*b*c - a*b*d - a*b*e - a*c*d - a*c*e - a*d*e - b*c*d - b*c*e - b*d*e - c*d*e
lvl4 = a*b*c*d + a*b*c*e + a*b*d*e + a*c*d*e + b*c*d*e
lvl5 = -a*b*c*d*e

Quintic_poly = x**5 + lvl1*x**4 + lvl2*x**3 + lvl3*x**2 + lvl4*x + lvl5

# 2nd level is even which possibly means it can be split in two

# this allows for the undermining of  the second layer if it can be discovered

# set1 and set2 have the components of lvl3
# my aim here is to use the quadratic to break lvl3 in half, and it is remotely possible since it is 10 terms
# the same thing was done with a quartic polynomial, which led to its  solution

# the reason for these sets is two make each set have 6 instances of each variable
set1 = ["abc", "abd", "abe", "acd", "ace"]
set2 = ["ade", "bcd", "bce", "bde", "cde"]
distributed_poorly = True
#while distributed_poorly:


#         -a*b**2*c + a*b*c*d + a*b*c*e + a*b*d**2 + 2*a*b*d*e + a*b*e**2 + a*c**2*d + a*c**2*e + a*c*d**2 + 3*a*c*d*e + a*c*e**2 + a*d**2*e + a*d*e**2 - b**2*d*e + b*c**2*d + b*c**2*e
#print(sympy.expand(mystery))