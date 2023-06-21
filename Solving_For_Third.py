import sympy
s0 = 0
s1 = 0
s2 = 0
r = 0
x = r**0.333333333333333*s1 + r**0.666666666666667*s2 + s0



s0, C0, s1, C1, s2, C2, r = sympy.symbols("s0 C0 s1 C1 s2 C2 r")
p2_0, p2_1, p2_2 = sympy.symbols("p2_0 p2_1 p2_2")
p3_0, p3_1, p3_2 = sympy.symbols("p3_0 p3_1 p3_2")

# C2 = -3*s0, C1 = 3*s0**2 - 3*r*s1*s2, C0 = 3*r*s0*s1*s2 - r**2*s2**3 - r*s1**3 - s0**3
P2_0 = 2*r*s1*s2 + s0**2
P2_1 = r*s2**2 + 2*s0*s1
P2_2 = 2*s0*s2 + s1**2


#
# 3*r*s0*s1*s2 - r**2*s2**3 - r*s1**3 - s0**3 = 9*r*s0*s1*s2 - P3_0
P3_0 = r**2*s2**3 + 6*r*s0*s1*s2 + r*s1**3 + s0**3
P3_1 = 3*r*s0*s2**2 + 3*r*s1**2*s2 + 3*s0**2*s1
P3_2 = 3*r*s1*s2**2 + 3*s0**2*s2 + 3*s0*s1**2


# x**3 + C2*x**2 + C1*x**1 + C0*x**0 = 0

# (C2*p2_2 + p3_2) / (C2*p2_1 + p3_1) = (s2) / (s1)

# s1*(C2*p2_2 + p3_2) = s2*(C2*p2_1 + p3_1)

equation1 = -C2*p2_1*s2 + C2*p2_2*s1 - p3_1*s2 + p3_2*s1

equations = [equation1]
variables = [C2]
result = sympy.solve(equations, variables)
C2 = result[C2]
# C2 = (p3_1*s2 - p3_2*s1)/(-p2_1*s2 + p2_2*s1)
C2_numerator, C2_denominator = sympy.fraction(C2)

replacements = []
for i in [C2_numerator, C2_denominator]:
    replacements.append(sympy.expand(i.subs([
                                 (p2_0, P2_0),
                                 (p2_1, P2_1),
                                 (p2_2, P2_2),
                                 (p3_0, P3_0),
                                 (p3_1, P3_1),
                                 (p3_2, P3_2)
                             ])))

C2_numerator, C2_denominator = replacements
C2_numerator = 3*r*s0*s2**3 - 3*s0*s1**3
C2_denominator = -r*s2**3 + s1**3

print(sympy.expand(P3_0 + P2_0*-3*s0 + (3*s0**2 - 3*r*s1*s2)*s0))
print(sympy.expand(P3_1 + P2_1*-3*s0 + (3*s0**2 - 3*r*s1*s2)*s1))
print(sympy.expand(P3_2 + P2_2*-3*s0 + (3*s0**2 - 3*r*s1*s2)*s2))



# Now fill out the values yourself and test the accuracy of the operations
# C2 = -3*s0, C1 = 3*s0**2 - 3*r*s1*s2, C0 = 3*r*s0*s1*s2 - r**2*s2**3 - r*s1**3 - s0**3

print(sympy.expand((-3 * s0)**3 + (3 * P2_0)**2 + (-3 * P3_0)))
C0 = 3*r*s0*s1*s2 - r**2*s2**3 - r*s1**3 - s0**3

print(C0)
print(P3_0)


