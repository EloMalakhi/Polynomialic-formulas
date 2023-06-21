import sympy

A, B, C, D, E, F = sympy.symbols("A B C D E F")
M1, M2, M3, M4 = sympy.symbols("M1 M2 M3 M4")
x = (-B + M1 + M2 + M3 + M4)/(5*A)

Fourth1, Fourth2, Fourth3, Fourth4, Fourth5 = sympy.symbols("Fourth1 Fourth2 Fourth3 Fourth4 Fourth5")


print(sympy.expand(A*x**5 + B*x**4 + C*x**3 + D*x**2 + E*x + F))


# x^5 C1x^4 C2x^3 C3x^2 C4x C5

# x = coef_1 + coef_2*Root + coef_3*Root**2 + coef_4*Root**3 + coef_5*Root**4
# x**2 = expr_2_1 + expr_2_2*Root + expr_2_3*Root**2 + expr_2_4*Root**3 + expr_2_5*Root**4
# x**3 = expr_3_1 + expr_3_2*Root + expr_3_3*Root**2 + expr_3_4*Root**3 + expr_3_5*Root**4
# x**4 = expr_4_1 + expr_4_2*Root + expr_4_3*Root**2 + expr_4_4*Root**3 + expr_4_5*Root**4
# x**5 = expr_5_1 + expr_5_2*Root + expr_5_3*Root**2 + expr_5_4*Root**3 + expr_5_5*Root**4

# (expr_5_5 + C1*expr_4_5 + C2*expr_3_5 + C3*expr_2_5) / (expr_5_2 + C1*expr_4_2 + C2*expr_3_2 + C3*expr_2_2) = coef_5/coef_2
# (expr_5_4 + C1*expr_4_4 + C2*expr_3_4 + C3*expr_2_4) / (expr_5_2 + C1*expr_4_2 + C2*expr_3_2 + C3*expr_2_2) = coef_4/coef_2
# (expr_5_3 + C1*expr_4_3 + C2*expr_3_3 + C3*expr_2_3) / (expr_5_2 + C1*expr_4_2 + C2*expr_3_2 + C3*expr_2_2) = coef_3/coef_2




