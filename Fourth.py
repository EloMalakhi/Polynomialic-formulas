import sympy

# S1, S2, S3, S4 = sympy.symbols("S1 S2 S3 S4")
a, b, c, d, e = sympy.symbols("a b c d e")
# M3, M4, M5 = sympy.symbols("M3 M4 M5")
# P1 = sympy.expand((b/a + S1)/2)
# P2 = sympy.expand((b/a - S1)/2)
# R1 = sympy.expand((c/a - M3 + S3)/2)
# R2 = sympy.expand((c/a - M3 - S3)/2)

# Hypothesis = sympy.expand(P1*R1 + P2*R2)
# Inside_S3_x_S1 = sympy.expand((b**2/a**2 - 4*M3)*((c/a - M3)**2 - 4*e/a))



# -M3*b/(2*a) + S1*S3/2 + b*c/(2*a**2)
# -M3*b/(2*a) + b*c/(2*a**2) .5√(-4*M3**3 + 8*M3**2*c/a + M3**2*b**2/a**2 + 16*M3*e/a - 4*M3*c**2/a**2 - 2*M3*b**2*c/a**3 - 4*b**2*e/a**3 + b**2*c**2/a**4)
# -M3*b/(2*a) + b*c/(2*a**2) .5√(-4*M4**3/27 - 4*M4**2*M5/9 + M4**2*b**2/(9*a**2) - 4*M4*M5**2/9 + 2*M4*M5*b**2/(9*a**2) + 16*M4*e/(3*a) + 4*M4*c**2/(9*a**2) - 2*M4*b**2*c/(9*a**3) - 4*M5**3/27 + M5**2*b**2/(9*a**2) + 16*M5*e/(3*a) + 4*M5*c**2/(9*a**2) - 2*M5*b**2*c/(9*a**3) + 32*c*e/(3*a**2) - 4*b**2*e/a**3 - 8*c**3/(27*a**3) + b**2*c**2/(9*a**4))
# M3 = (2*c/(3*a) + M4/3 + M5/3)
# -M3*b/(2*a) + b*c/(2*a**2) .5√(-4*M1/27 - 4*M2*M4/9 + M4**2*b**2/(9*a**2) - 4*M2*M5/9 + 2*M2*b**2/(9*a**2) + 16*M4*e/(3*a) + 4*M4*c**2/(9*a**2) - 2*M4*b**2*c/(9*a**3) + M5**2*b**2/(9*a**2) + 16*M5*e/(3*a) + 4*M5*c**2/(9*a**2) - 2*M5*b**2*c/(9*a**3) + 32*c*e/(3*a**2) - 4*b**2*e/a**3 - 8*c**3/(27*a**3) + b**2*c**2/(9*a**4))

# M1 = 72*c*e/a**2 - 27*d**2/a**2 - 27*b**2*e/a**3 + 9*b*c*d/a**3 - 2*c**3/a**3
# M2 = 12*e/a - 3*b*d/a**2 + c**2/a**2

# -M3*b/(2*a) + b*c/(2*a**2) + .5√(M4**2*b**2/(9*a**2) + 4*M4*b*d/(3*a**2) - 2*M4*b**2*c/(9*a**3) + M5**2*b**2/(9*a**2) + 4*M5*b*d/(3*a**2) - 2*M5*b**2*c/(9*a**3) + 4*d**2/a**2 + 8*b**2*e/(3*a**3) - 4*b*c*d/(3*a**3) - 2*b**3*d/(3*a**4) + b**2*c**2/(3*a**4))
# -M3*b/(2*a) + b*c/(2*a**2) + .5√((2*d/a - b*c/(3*a**2) + (b/(3*a))*(M4 + M5))**2)
# -M3*b/(2*a) + b*c/(2*a**2) + .5((2*d/a - b*c/(3*a**2) + (b/(3*a))*(M4 + M5))
# -(2*c/(3*a) + M4/3 + M5/3)*b/(2*a) + b*c/(2*a**2) + .5((2*d/a - b*c/(3*a**2) + (b/(3*a))*(M4 + M5))
#print(sympy.expand(-(2*c/(3*a) + M4/3 + M5/3)*b/(2*a) + b*c/(2*a**2) + ((d/a - b*c/(6*a**2) + (b/(6*a))*(M4 + M5)))))


# Now that we have proved that P1*R1 + P2*R2 = d/a, we can solve for s1, s2, s3, and s4
# P1 = sympy.expand((b/a + S1)/2)
# P2 = sympy.expand((b/a - S1)/2)
# R1 = sympy.expand((c/a - M3 + S3)/2)
# R2 = sympy.expand((c/a - M3 - S3)/2)

# P1 = -a - b
# P2 = -c - d
# R1 = cd
# R2 = ab

# P1**2 = aa 2ab bb
# √(P1**2 - 4R2) = a - b or b - a
# P1 + √(P1**2 - 4R2) = -2b or -2a
# (-P1 ± √(P1**2 - 4R2))/2 = a or b
# (-P2 ± √(P2**2 - 4R1))/2 = c or d

# the four solutions are 
# (-P1 + √(P1**2 - 4R1))/2
# (-P1 - √(P1**2 - 4R1))/2
# (-P2 - √(P2**2 - 4R2))/2
# (-P2 + √(P2**2 - 4R2))/2

# Testing
M3, M4, M5 =  sympy.symbols('M3 M4 M5')
S1, S2, S3, S4 = sympy.symbols('S1 S2 S3 S4')
R1, R2, P1, P2 = sympy.symbols('R1 R2 P1 P2')


sol1 = (P1 + S1)/2
sol2 = (P1 - S1)/2
sol3 = (P2 - S2)/2
sol4 = (P2 + S2)/2

t1 = sol1 + sol2 + sol3 + sol4
t1 = t1.subs([(P1, (-b/a + S3)/2), (P2, (-b/a - S3)/2)])

t2 = sympy.expand((sol1 + sol2)*(sol3 + sol4) + sol1*sol2 + sol3*sol4)
t2 = t2.subs([(S1**2, P1**2 - 4*R1), (S2**2, P2**2 - 4*R2)])
t2 = sympy.expand(t2.subs([(P1, (-b/a + S3)/2), (P2, (-b/a - S3)/2)]))
t2 = sympy.expand(t2.subs([(R1, (c/a - M3 + S4)/2), (R2, (c/a - M3 - S4)/2)]))
t2 = sympy.expand(t2.subs([(S3**2, b**2/a**2 - 4*M3)]))

t3 = sympy.expand(- sol1*sol2*(sol3 + sol4) - sol3*sol4*(sol1 + sol2))
t3 = sympy.expand(t3.subs([(S1**2, P1**2 - 4*R1), (S2**2, P2**2 - 4*R2)]))
t3 = sympy.expand(t3.subs([(P1, (-b/a + S3)/2), (P2, (-b/a - S3)/2)]))
t3 = sympy.expand(t3.subs([(R1, (c/a - M3 + S4)/2), (R2, (c/a - M3 - S4)/2)]))
t3 = sympy.expand(t3.subs([(S3*S4, 2*d/a - b*c/(3*a**2) + (b/(3*a))*(M4 + M5))]))
t3 = sympy.expand(t3.subs([(M3, 2*c/(3*a) + M4/3 + M5/3)]))

t4 = sympy.expand(sol1*sol2*sol3*sol4)
t4 = sympy.expand(t4.subs([(S1**2, P1**2 - 4*R1), (S2**2, P2**2 - 4*R2)]))
t4 = sympy.expand(t4.subs([(R1, (c/a - M3 + S4)/2), (R2, (c/a - M3 - S4)/2)]))
t4 = sympy.expand(t4.subs([(S4**2, (c/a - M3)**2 - 4*e/a)]))


