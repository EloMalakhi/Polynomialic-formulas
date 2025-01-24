import sympy


a, b, c, d, e = sympy.symbols('a b c d e')

# the four solutions are 
# (P1 + √(P1**2 - 8aR1))/4a
# (P1 - √(P1**2 - 8aR1))/4a
# (P2 - √(P2**2 - 8aR2))/4a
# (P2 + √(P2**2 - 8aR2))/4a

# definitions
# P1 = (-b + S3)
# P2 = (-b - S3)
# R1 = (c - M3 + S4)
# R2 = (c - M3 - S4)

# S3 = √(b**2 - 4aM3)
# S4 = √((c - M3)**2 - 4ae)
# M3 = 2c/3 + M4/3 + M5/3
# M4 = cube_root((M1 + M6)/2)
# M5 = cube_root((M1 - M6)/2)
# M6 = √(M1**2 - 4M2^3)
# M1 = 72ace - 27add - 27bbe + 9bcd - 2ccc
# M2 = 12ae - 3bd + cc


# Testing

# (x - z1)(x - z2)(x - z3)(x - z4) = 
# x^4
# +  (-z1 - z2 - z3 - z4)x^3
# + [(z1 + z2)(z3 + z4) + z1z2 + z3z4]x^2
# + [-z1z2(z3 + z4) - z3z4(z1 + z2)]x
# + z1z2z3z4


M1, M6 = sympy.symbols('M1 M6')
M3, M4, M5 =  sympy.symbols('M3 M4 M5')
S1, S2, S3, S4 = sympy.symbols('S1 S2 S3 S4')
R1, R2, P1, P2 = sympy.symbols('R1 R2 P1 P2')



sol1 = (P1 + S1)/4/a
sol2 = (P1 - S1)/4/a
sol3 = (P2 - S2)/4/a
sol4 = (P2 + S2)/4/a

t1 = -sol1 - sol2 - sol3 - sol4
t1 = sympy.expand(t1.subs([(P1, -b + S3), (P2, -b - S3)]))
print(f"First coefficient operation yields = {t1}\n")

t2 = sympy.expand((sol1 + sol2)*(sol3 + sol4) + sol1*sol2 + sol3*sol4)
t2 = t2.subs([(S1**2, P1**2 - 8*a*R1), (S2**2, P2**2 - 8*a*R2)])
t2 = sympy.expand(t2.subs([(P1, -b + S3), (P2, -b - S3)]))
t2 = sympy.expand(t2.subs([(R1, c - M3 + S4), (R2, c - M3 - S4)]))
t2 = sympy.expand(t2.subs([(S3**2, b**2 - 4*a*M3)]))
print(f"Second coefficient operation yields = {t2}\n")

print(f"Cut away view of S3*S4 substitution\n")
t3 = sympy.expand(- sol1*sol2*(sol3 + sol4) - sol3*sol4*(sol1 + sol2))
t3 = sympy.expand(t3.subs([(S1**2, P1**2 - 8*a*R1), (S2**2, P2**2 - 8*a*R2)]))
t3 = sympy.expand(t3.subs([(P1, -b + S3), (P2, -b - S3)]))
t3 = sympy.expand(t3.subs([(R1, c - M3 + S4), (R2, c - M3 - S4)]))
print(f"        part way completion of third operation yields {t3}\n")

cut_away = S3**2*S4**2
cut_away = sympy.expand(cut_away.subs([(S3**2*S4**2, (b**2 - 4*a*M3)*(c**2 - 2*c*M3 + M3**2 - 4*a*e))]))
cut_away = sympy.expand(cut_away.subs([(M3**3, (2*c/3 + M4/3 + M5/3)**3)]))
cut_away = sympy.expand(cut_away.subs([(M3**2, (2*c/3 + M4/3 + M5/3)**2)]))
cut_away = sympy.expand(cut_away.subs([(M4*M5, 12*a*e - 3*b*d + c**2)]))
cut_away = sympy.expand(cut_away.subs([(M4**3, (M1 + M6)/2)]))
cut_away = sympy.expand(cut_away.subs([(M5**3, (M1 - M6)/2)]))
cut_away = sympy.expand(cut_away.subs([(M3, 2*c/3 + M4/3 + M5/3)]))
cut_away = sympy.expand(cut_away.subs(M1, 72*a*c*e - 27*a*d*d - 27*b*b*e + 9*b*c*d - 2*c*c*c))

print("        End result: S3*S4 = 2*a*d - b*c/3 + b*(M4 + M5)/3\n")
print(f"        Present result S3*S4 = √({cut_away})\n")
print()
alternate_string = sympy.expand((2*a*d - b*c/3 + b*(M4 + M5)/3)**2)
alternate_string = sympy.expand(alternate_string.subs([(M4*M5, 12*a*e - 3*b*d + c**2)]))
print(f"        Expanded form of guess**2 (2*a*d - b*c/3 + b*(M4 + M5)/3)**2 = {alternate_string}")
print()
print(f"        difference between S3**2*S4**2 and guess**2 = {sympy.expand(cut_away - alternate_string)}")
print(f"        replacing S3*S4 with 2*a*d - b*c/3 + b*(M4 + M5)/3\n")
print()
t3 = sympy.expand(t3.subs([(S3*S4, 2*a*d - b*c/3 + b*(M4 + M5)/3)]))
t3 = sympy.expand(t3.subs([(M3, 2*c/3 + M4/3 + M5/3)]))
print(f"Third coefficient operation yields = {t3}\n")




t4 = sympy.expand(sol1*sol2*sol3*sol4)
t4 = sympy.expand(t4.subs([(S1**2, P1**2 - 8*a*R1), (S2**2, P2**2 - 8*a*R2)]))
t4 = sympy.expand(t4.subs([(R1, (c - M3 + S4)), (R2, (c - M3 - S4))]))
t4 = sympy.expand(t4.subs([(S4**2, (c - M3)**2 - 4*a*e)]))
print(f"Fourth coefficient operation yields = {t4}\n")

