import sympy
s0 = 0
s1 = 0
r = 0
x = r**0.5*s1 + s0

P2_0 = r*s1**2 + s0**2
P2_1 = 2*s0*s1

s0, C0, s1, C1 = sympy.symbols("s0 C0 s1 C1")
p2_0, p2_1 = sympy.symbols("p2_0 p2_1")


# x**5 + C1*x**1 + C0*x**0 = 0




equations = []
variables = []
result = sympy.solve(equations, variables)

# C1 = -2*s0, C0 = s0**2 - s1**2*r
