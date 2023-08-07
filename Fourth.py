import sympy


a, b, c, d, e = sympy.symbols('a b c d e')

# the four solutions are 
# (P1 + √(P1**2 - 4R1))/2
# (P1 - √(P1**2 - 4R1))/2
# (P2 - √(P2**2 - 4R2))/2
# (P2 + √(P2**2 - 4R2))/2

# definitions
# P1 = (-b/a + S3)/2
# P2 = (-b/a - S3)/2
# R1 = (c/a - M3 + S4)/2
# R2 = (c/a - M3 - S4)/2

# S3 = √(b**2/a**2 - 4M3)
# S4 = √((c/a - M3)**2 - 4e/a)
# M3 = 2c/(3a) + M4/3 + M5/3
# M4 = cube_root((M1 + M6)/2)
# M5 = cube_root((M1 - M6)/2)
# M6 = √(M1**2 - 4M2^3)
# M1 = 72ce/aa - 27dd/aa - 27bbe/aaa + 9bcd/aaa - 2ccc/aaa
# M2 = 12e/a - 3bd/aa + cc/aa


# Testing

# (x - z1)(x - z2)(x - z3)(x - z4) = 
# x^4
# +  (-z1 - z2 - z3 - z4)x^3
# + [(z1 + z2)(z3 + z4) + z1z2 + z3z4]x^2
# + [-z1z2(z3 + z4) - z3z4(z1 + z2)]x
# + z1z2z3z4

M3, M4, M5 =  sympy.symbols('M3 M4 M5')
S1, S2, S3, S4 = sympy.symbols('S1 S2 S3 S4')
R1, R2, P1, P2 = sympy.symbols('R1 R2 P1 P2')



sol1 = (P1 + S1)/2
sol2 = (P1 - S1)/2
sol3 = (P2 - S2)/2
sol4 = (P2 + S2)/2

t1 = -sol1 - sol2 - sol3 - sol4
t1 = t1.subs([(P1, (-b/a + S3)/2), (P2, (-b/a - S3)/2)])
print(t1)
t2 = sympy.expand((sol1 + sol2)*(sol3 + sol4) + sol1*sol2 + sol3*sol4)
t2 = t2.subs([(S1**2, P1**2 - 4*R1), (S2**2, P2**2 - 4*R2)])
t2 = sympy.expand(t2.subs([(P1, (-b/a + S3)/2), (P2, (-b/a - S3)/2)]))
t2 = sympy.expand(t2.subs([(R1, (c/a - M3 + S4)/2), (R2, (c/a - M3 - S4)/2)]))
t2 = sympy.expand(t2.subs([(S3**2, b**2/a**2 - 4*M3)]))
print(t2)
t3 = sympy.expand(- sol1*sol2*(sol3 + sol4) - sol3*sol4*(sol1 + sol2))
t3 = sympy.expand(t3.subs([(S1**2, P1**2 - 4*R1), (S2**2, P2**2 - 4*R2)]))
t3 = sympy.expand(t3.subs([(P1, (-b/a + S3)/2), (P2, (-b/a - S3)/2)]))
t3 = sympy.expand(t3.subs([(R1, (c/a - M3 + S4)/2), (R2, (c/a - M3 - S4)/2)]))
t3 = sympy.expand(t3.subs([(S3*S4, 2*d/a - b*c/(3*a**2) + (b/(3*a))*(M4 + M5))]))
t3 = sympy.expand(t3.subs([(M3, 2*c/(3*a) + M4/3 + M5/3)]))
print(t3)
t4 = sympy.expand(sol1*sol2*sol3*sol4)
t4 = sympy.expand(t4.subs([(S1**2, P1**2 - 4*R1), (S2**2, P2**2 - 4*R2)]))
t4 = sympy.expand(t4.subs([(R1, (c/a - M3 + S4)/2), (R2, (c/a - M3 - S4)/2)]))
t4 = sympy.expand(t4.subs([(S4**2, (c/a - M3)**2 - 4*e/a)]))
print(t4)

