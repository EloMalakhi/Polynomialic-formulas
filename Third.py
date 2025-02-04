import sympy

# 2 Vertices come as a result of b**2 - 3*a*c > 0
# 1 Vertex comes as a result of b**2 = 3*a*c
# else 0 Vertex

# 3 solutions come as a result of d(-27aad + 18abc - 4bbb) + c**2(b**2 - 4ac) > 0
# 2 solutions come as a result of d(-27aad + 18abc - 4bbb) + c**2(b**2 - 4ac) = 0 and d - b*c/(3*a) + 2*b**3/(27*a**2) ≠ 0
# else 1 solution



# Proofs

# Here is a polynomial of degree 3
A, B, C, D, x = sympy.symbols("A B C D x")
polynomial = A*x**3 + B*x**2 + C*x + D

# this polynomial has three solutions a, b, c
a, b, c = sympy.symbols("a b c")
the_B_coefficient_divided_by_A = -a - b - c
the_C_coefficient_divided_by_A = c*(a + b) + a*b
the_D_coefficient_divided_by_A = -a*b*c

# Initializing some symbols used for memory substitution:
#    It will make the expressions easier to read
M1, M2, M3, M4, M5, S1 = sympy.symbols("M1 M2 M3 M4 M5 S1")

# Initializing some symbols used for definition substitution:
#    It will make the expressions easier to read


"""Defining what these symbols mean:

M1 = 9*A*B*C - 27*A*A*D - 2*B**3
M2 = B*B - 3*A*C
M3 = ((M1 + M5)/2)**(1/3)
M4 = ((M1 - M5)/2)**(1/3)
M5 = (M1**2 - 4*M2**3)**(1/2)
S1 = (2*M2/3 - M4**2/3 - M5**2/3)**(1/2)


"""

# Initializing a memory dictionary:
Mem = {}

# Putting some substitutions into the memory dictionary:
Mem[M1] = 9*A*B*C - 27*A*A*D - 2*B**3
Mem[M2] = B*B - 3*A*C
Mem[M3**3] = (M1 + M5)/2
Mem[M4**3] = (M1 - M5)/2
Mem[M5**2] = M1**2 - 4*M2**3
Mem[M3**2*M4] = M2*M3
Mem[M3*M4**2] = M2*M4
Mem[M3*M4] = M2
Mem[S1**2] = 2*M2/3 - (M3**2)/3 - (M4**2)/3


# showing what the three solutions are:

a = (-B + M3 + M4)/(3*A)
b = (-2*B/3 - M3/3 - M4/3 + S1)/(2*A)
c = (-2*B/3 - M3/3 - M4/3 - S1)/(2*A)





class ShowProofs(object):
    def __init__(self, type_of_mechanic, end_of_proof, start_expression, memory_substitutions, definition_substitutions):
        self.type_of_mechanic = type_of_mechanic
        self.end_of_proof = end_of_proof
        self.start_expression = start_expression
        self.memory_substitutions = memory_substitutions
        self.definition_substitutions = definition_substitutions

    def prove(self):
        print(f"Showing that {self.type_of_mechanic} = {self.end_of_proof}\n")
        print(f"{self.type_of_mechanic} = {self.start_expression}\n")
        for i in self.memory_substitutions:
            print(f"replacing {i} with {self.definition_substitutions[i]}")
            self.start_expression = sympy.expand(self.start_expression.subs([(i, self.definition_substitutions[i])]))
        return self.start_expression
    
print("###########################################")
B_divided_by_A_case = ShowProofs("-a -b -c", B/A, sympy.expand(-a -b -c), [], Mem)
result = B_divided_by_A_case.prove()
print(f"\n{result}")
print("###########################################")
input("")


print("###########################################")
C_divided_by_A_case = ShowProofs("c*(a + b) + a*b", C/A, sympy.expand(a*(c + b) + c*b), [M3*M4, S1**2, M2], Mem)
result = C_divided_by_A_case.prove()
print(f"\n{result}")
print("###########################################")
input("")

print("###########################################")
D_divided_by_A_case = ShowProofs("-a*b*c", D/A, sympy.expand(-a*b*c), [S1**2, M3*M4, M4**3, M3**3, M1, M2], Mem)
result = D_divided_by_A_case.prove()
print(f"\n{result}")
print("###########################################")
input()


print("###########################################")
print("Hence the three solutions are:\n")
print(f"{a.subs([(S1, f'sqrt({Mem[S1**2]})')])}")
print(f"{b.subs([(S1, f'sqrt({Mem[S1**2]})')])}")
print(f"{c.subs([(S1, f'sqrt({Mem[S1**2]})')])}")
print("###########################################")
input()
print("###########################################")    
print(f"Definitions\n")
print(f"S1 = sqrt({Mem[S1**2]})")
print(f"M3 = {Mem[M3**3]}")
print(f"M4 = ({Mem[M4**3]})**(1/3)")
print(f"M5 = ({Mem[M5**2]})**(1/2)")
print(f"M1 = {Mem[M1]}")
print(f"M2 = {Mem[M2]}")

# Output

# ###########################################
# Showing that -a -b -c = B/A

# -a -b -c = B/A


# B/A
# ###########################################

# ###########################################
# Showing that c*(a + b) + a*b = C/A

# c*(a + b) + a*b = B**2/(3*A**2) - M3**2/(12*A**2) - M3*M4/(6*A**2) - M4**2/(12*A**2) - S1**2/(4*A**2)

# replacing M3*M4 with M2
# replacing S1**2 with 2*M2/3 - M3**2/3 - M4**2/3
# replacing M2 with -3*A*C + B**2

# C/A
# ###########################################

# ###########################################
# Showing that -a*b*c = D/A

# -a*b*c = B**3/(27*A**3) - B*M3**2/(36*A**3) - B*M3*M4/(18*A**3) - B*M4**2/(36*A**3) - B*S1**2/(12*A**3) - M3**3/(108*A**3) - M3**2*M4/(36*A**3) - M3*M4**2/(36*A**3) + M3*S1**2/(12*A**3) - M4**3/(108*A**3) + M4*S1**2/(12*A**3)

# replacing S1**2 with 2*M2/3 - M3**2/3 - M4**2/3
# replacing M3*M4 with M2
# replacing M4**3 with M1/2 - M5/2
# replacing M3**3 with M1/2 + M5/2
# replacing M1 with -27*A**2*D + 9*A*B*C - 2*B**3
# replacing M2 with -3*A*C + B**2

# D/A
# ###########################################

# ###########################################
# Hence the three solutions are:

# (-B + M3 + M4)/(3*A)
# (-2*B/3 - M3/3 - M4/3 + sqrt(2*M2/3 - M3**2/3 - M4**2/3))/(2*A)
# (-2*B/3 - M3/3 - M4/3 - sqrt(2*M2/3 - M3**2/3 - M4**2/3))/(2*A)
# ###########################################

# ###########################################
# Definitions

# S1 = sqrt(2*M2/3 - M3**2/3 - M4**2/3)
# M3 = M1/2 + M5/2
# M4 = (M1/2 - M5/2)**(1/3)
# M5 = (M1**2 - 4*M2**3)**(1/2)
# M1 = -27*A**2*D + 9*A*B*C - 2*B**3
# M2 = -3*A*C + B**2