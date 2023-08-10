import sympy
a, b, c, d, e = sympy.symbols('a b c d e')
M1, M2, M3, M4, M5, M6 = sympy.symbols('M1 M2 M3 M4 M5 M6')
S1, S2, S3, S4, P1, P2, P3, P4, P5 = sympy.symbols('S1 S2 S3 S4 P1 P2 P3 P4 P5')

p3_squared = P1**2 - 4*P4 - 4*P5
p1 = P2 - b/(2*a)
p2_squared = b*b/(4*a*a) - M3
p4 = c/(2*a) - M3/2
m3 = 2*c/(3*a) + M4/3 + M5/3
p2_p5 = d/(2*a) - b*c/(12*a*a) + b*M4/(12*a) + b*M5/(12*a)
p5_squared = P4**2 - e/a
p4_squared = sympy.expand((c/(2*a) - M3/2)**2)

x = (P1 + P3)/2

expanded = sympy.expand(a*x**4 + b*x**3 + c*x**2 + d*x + e)
Doc1 = """x = (P1 + P3)/2
f(x) = P1**4*a/16 + P1**3*P3*a/4 + P1**3*b/8 + 3*P1**2*P3**2*a/8 + 3*P1**2*P3*b/8 + P1**2*c/4 + P1*P3**3*a/4 + 3*P1*P3**2*b/8 + P1*P3*c/2 
      + P1*d/2 + P3**4*a/16 + P3**3*b/8 + P3**2*c/4 + P3*d/2 + e
root_coefficient = P1**3*a/4 + 3*P1**2*b/8 + P1*P3**2*a/4 + P1*c/2 + P3**2*b/8 + d/2
simple_coefficient = P1**4*a/16 + P1**3*b/8 + 3*P1**2*P3**2*a/8 + P1**2*c/4 + 3*P1*P3**2*b/8 + P1*d/2 + P3**4*a/16 + P3**2*c/4 + e
f(x) = ax^4 + bx^3 + cx^2 + dx + e
f(x) = simple_coefficient + root_coefficient*P3

P3 is the most complex root of x
therefore it can't be neutralized by any group of terms, it must have a coefficient of 0
P2*P5 can be proven to be (2*d/a - b*c/(3*a**2) + b*M4/(3*a) + b*M5/(3*a))/4 but we won't go into it now."""

root_coefficient = P1**3*a/4 + 3*P1**2*b/8 + P1*P3**2*a/4 + P1*c/2 + P3**2*b/8 + d/2
simple_coefficient = P1**4*a/16 + P1**3*b/8 + 3*P1**2*P3**2*a/8 + P1**2*c/4 + 3*P1*P3**2*b/8 + P1*d/2 + P3**4*a/16 + P3**2*c/4 + e


root_coefficient_replacements = [(P3**2, p3_squared), 
                                 (P1, p1), (P2**2, p2_squared), 
                                 (P2**3, P2*p2_squared), 
                                 (P4, p4), (M3, m3), 
                                 (P2*P5, p2_p5)]

simple_coefficient_replacements = [(P3**2, p3_squared),
                                   (P1**4, P1**3*p1),
                                   (P1**3, P1**2*p1),
                                   (P2**2, p2_squared),
                                   (P4, p4), (P1**2, P1*p1),
                                   (P5**2, p5_squared),
                                   (P2*P5, p2_p5),
                                   (P1*P2*c/2, P2*p1*c/2), 
                                   (P4**2, p4_squared),
                                   (P2**2, p2_squared), 
                                   (P1*b*c/(3*a), p1*b*c/(3*a)), 
                                   (P1*P5, p1*P5), 
                                   (P1*P2, p1*P2), 
                                   (P2**2, p2_squared), 
                                   (M3*P1*b/2, M3*p1*b/2), 
                                   (M4*P1*b/6, M4*p1*b/6), 
                                   (M3*P2*b/4, m3*P2*b/4), 
                                   (M5*P1*b/6, M5*p1*b/6), 
                                   (M3*b**2, m3*b**2), 
                                   (P1*d, p1*d), 
                                   (P2*P5, p2_p5), 
                                   (M3*P5, m3*P5)]

print(Doc1)
input("")
for i in root_coefficient_replacements:
    root_coefficient = sympy.expand(root_coefficient.subs([(i[0], i[1])]))
    print(f"replacing {i[0]} with {i[1]}: ")
    print(f"   {root_coefficient}")
    input("")

print("SIMPLIFYING SIMPLE COEFFICIENT")
for i in simple_coefficient_replacements:
    simple_coefficient = sympy.expand(simple_coefficient.subs([(i[0], i[1])]))
    print(f"replacing {i[0]} with {i[1]}: ")
    print(f"   {simple_coefficient}")
    input("")

Doc2 = """for the formula to be proven this last part must be simplified to 0, assimilating it into parts gives:
P2*(-M4*b/12 - M5*b/12 - d/2 + b*c/(12*a)) + P5*(-M4*a/3 - M5*a/3 - 2*c/3 + b**2/(4*a))
we know that P2*P5 = d/(2*a) - b*c/(12*a**2) + b*M4/(12*a) + b*M5/(12*a)
therefore -a*P2*P5 = -d/2 + b*c/(12*a) -  b*M4/12 - b*M5/12

substituting this into the formula gives:
P5*(-M4*a/3 - M5*a/3 - 2*c/3 + b**2/(4*a) - a*P2**2)

setting simple_coefficient to P5*(-M4*a/3 - M5*a/3 - 2*c/3 + b**2/(4*a) - a*P2**2)
replacing P2**2 with b*b/(4*a*a) - M3
replacing M3*P5*a with {m3*P5*a}"""
simple_coefficient = sympy.expand(P5*(-M4*a/3 - M5*a/3 - 2*c/3 + b**2/(4*a) - a*P2**2))
simple_coefficient = sympy.expand(simple_coefficient.subs([(P2**2, p2_squared)]))
simple_coefficient = sympy.expand(simple_coefficient.subs([(M3*P5*a, m3*P5*a)]))
print(Doc2)
input('')
print(simple_coefficient)
# 0



