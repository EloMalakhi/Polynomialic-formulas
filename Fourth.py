import sympy


# Proofs

# Here is a polynomial of degree 4
A, B, C, D, E, x = sympy.symbols("A B C D E x")
polynomial = A*x**4 + B*x**3 + C*x**2 + D*x + E

# this polynomial has four solutions a, b, c, and d
a, b, c, d = sympy.symbols("a b c d")
the_B_coefficient_divided_by_A = -a - b - c - d
the_C_coefficient_divided_by_A = (a + b)*(c + d) + a*b + c*d
the_D_coefficient_divided_by_A = -a*b*(c + d) - c*d*(a + b)
the_E_coefficient_divided_by_A = a*b*c*d

# Initializing some symbols used for memory substitution:
#    It will make the expressions easier to read
M1, M2, M3, M4, M5, M6 = sympy.symbols("M1 M2 M3 M4 M5 M6")

# Initializing some symbols used for definition substitution:
#    It will make the expressions easier to read
S1, S2, S3, P1 = sympy.symbols("S1 S2 S3 P1")

"""Defining what these symbols mean:

M1 = 72*C*E/A**2 - 27*D**2/A**2 - 27*B**2*E/A**3 + 9*B*C*D/A**3 - 2*C**3/A**3
M2 = 12*E/A - 3*B*D/A**2 + C**2/A**2
M3 = (2*C/A + M4 + M5)
M4 = (M1 + M6)/2
M5 = (M1 - M6)/2
M6 = sqrt(M1**2 - 4*M2**3)

P1 = C - A*M3

S1 = sqrt(B*B - 4*A*A*M3)
S2 = sqrt( 
            (-B + S1)**2 - 4*A*(4*A*D + 2*(-B + S1)*P1)/S1)
         )
S3 = sqrt(
            (-B - S1)**2 + 4*A*(4*A*D + 2*(-B - S1)*P1)/S1
         )
"""

# Initializing a memory dictionary:
Mem = {}

# Putting some substitutions into the memory dictionary:
Mem[M1] = 72*C*E/A**2 - 27*D**2/A**2 - 27*B**2*E/A**3 + 9*B*C*D/A**3 - 2*C**3/A**3
Mem[M2] = 12*E/A - 3*B*D/A**2 + C**2/A**2
Mem[M3] = (2*C/A + M4 + M5)/3
Mem[M4**3] = (M1 + M6)/2
Mem[M5**3] = (M1 - M6)/2
Mem[M6**2] = M1**2 - 4*M2**3
Mem[P1] = C - A*M3
Mem[S1**2] = B*B - 4*A*A*M3
Mem[S2**2] = (-B + S1)**2 - 4*A*(4*A*D + 2*(-B + S1)*P1)/S1
Mem[S3**2] = (-B - S1)**2 + 4*A*(4*A*D + 2*(-B - S1)*P1)/S1
Mem[M4*M5] = M2
Mem[M4**2*M5] = M2*M4
Mem[M4*M5**2] = M2*M5
Mem[(-16*A**4*M3 + 4*A**2*B**2)] = (16*A**2)


# showing what the four solutions are:

a = ((-B + S1) - S2)/(4*A)
b = ((-B + S1) + S2)/(4*A)
c = ((-B - S1) - S3)/(4*A)
d = ((-B - S1) + S3)/(4*A)

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
B_divided_by_A_case = ShowProofs("-a -b -c -d", B/A, sympy.expand(-a -b -c -d), [], Mem)
result = B_divided_by_A_case.prove()
print(f"\n{result}")
print("###########################################")
input("")


print("###########################################")
C_divided_by_A_case = ShowProofs("(a + b)*(c + d) + a*b + c*d", C/A, sympy.expand((a + b)*(c + d) + a*b + c*d), [S3**2, S2**2, S1**2, P1], Mem)
result = C_divided_by_A_case.prove()
print(f"\n{result}")
print("###########################################")
input("")

print("###########################################")
D_divided_by_A_case = ShowProofs("-a*b*(c + d) - c*d*(a + b)", D/A, sympy.expand(-a*b*(c + d) - c*d*(a + b)), [S3**2, S2**2], Mem)
result = D_divided_by_A_case.prove()
print(f"\n{result}")
print("###########################################")
input()

print("###########################################")
E_divided_by_A_case = ShowProofs("a*b*c*d", E/A, sympy.expand(a*b*c*d), [S3**2, S2**2], Mem)
result = E_divided_by_A_case.prove()
numer  = sympy.expand(result*S1**2)
denom  = sympy.expand(S1**2)
print("splitting the problem up into a fraction:\n")
print(f"numerator = {numer}\n")
print(f"denominator = {denom}")
print("###########################################")
input()

print("###########################################")
E_divided_by_A_case_numerator = ShowProofs("numerator of a*b*c*d", -4*A*E*M4/3 - 4*A*E*M5/3 - 8*C*E/3 + B**2*E/A, numer, [S1**2, P1, M3, M4**3, M5**3, M4**2*M5, M4*M5**2, M1, M2], Mem)
numer = E_divided_by_A_case_numerator.prove()
print(f"\n{numer}")
print("###########################################")
input()

print("###########################################")
E_divided_by_A_case_denominator = ShowProofs("denominator of a*b*c*d", -4*A**2*M4/3 - 4*A**2*M5/3 - 8*A*C/3 + B**2, denom, [S1**2, P1, M3], Mem)
denom = E_divided_by_A_case_denominator.prove()
print(f"\n{denom}")
print("###########################################")
input()

print("###########################################")
print(f"{numer}    /    {denom}     = \n\nE/A")
print("###########################################")
input()

print("###########################################")
print("Hence the four solutions are:\n")
print(f"{a.subs([(S2, f'sqrt({Mem[S2**2]})')])}")
print(f"{b.subs([(S2, f'sqrt({Mem[S2**2]})')])}")
print(f"{c.subs([(S3, f'sqrt({Mem[S3**2]})')])}")
print(f"{d.subs([(S3, f'sqrt({Mem[S3**2]})')])}")
print("###########################################")
input()
print("###########################################")    
print(f"Definitions\n")
print(f"S1 = sqrt({Mem[S1**2]})")
print(f"P1 = {Mem[P1]}")
print(f"M3 = {Mem[M3]}")
print(f"M4 = ({Mem[M4**3]})**(1/3)")
print(f"M5 = ({Mem[M5**3]})**(1/3)")
print(f"M6 = sqrt({Mem[M6**2]})")
print(f"M1 = {Mem[M1]}")
print(f"M2 = {Mem[M2]}")

# Output

# ###########################################
# Showing that -a -b -c -d = B/A

# -a -b -c -d = B/A


# B/A
# ###########################################

# ###########################################
# Showing that (a + b)*(c + d) + a*b + c*d = C/A

# (a + b)*(c + d) + a*b + c*d = 3*B**2/(8*A**2) - S1**2/(8*A**2) - S2**2/(16*A**2) - S3**2/(16*A**2)

# replacing S3**2 with 4*A*(4*A*D + P1*(-2*B - 2*S1))/S1 + (-B - S1)**2
# replacing S2**2 with -4*A*(4*A*D + P1*(-2*B + 2*S1))/S1 + (-B + S1)**2
# replacing S1**2 with -4*A**2*M3 + B**2
# replacing P1 with -A*M3 + C

# C/A
# ###########################################

# ###########################################
# Showing that -a*b*(c + d) - c*d*(a + b) = D/A

# -a*b*(c + d) - c*d*(a + b) = B**3/(16*A**3) - B*S1**2/(16*A**3) - B*S2**2/(32*A**3) - B*S3**2/(32*A**3) - S1*S2**2/(32*A**3) + S1*S3**2/(32*A**3)

# replacing S3**2 with 4*A*(4*A*D + P1*(-2*B - 2*S1))/S1 + (-B - S1)**2
# replacing S2**2 with -4*A*(4*A*D + P1*(-2*B + 2*S1))/S1 + (-B + S1)**2

# D/A
# ###########################################

# ###########################################
# Showing that a*b*c*d = E/A

# a*b*c*d = B**4/(256*A**4) - B**2*S1**2/(128*A**4) - B**2*S2**2/(256*A**4) - B**2*S3**2/(256*A**4) - B*S1*S2**2/(128*A**4) + B*S1*S3**2/(128*A**4) + S1**4/(256*A**4) - S1**2*S2**2/(256*A**4) - S1**2*S3**2/(256*A**4) + S2**2*S3**2/(256*A**4)

# replacing S3**2 with 4*A*(4*A*D + P1*(-2*B - 2*S1))/S1 + (-B - S1)**2
# replacing S2**2 with -4*A*(4*A*D + P1*(-2*B + 2*S1))/S1 + (-B + S1)**2
# splitting the problem up into a fraction:

# numerator = -D**2 + B*D*P1/A - B**2*P1**2/(4*A**2) + P1**2*S1**2/(4*A**2)

# denominator = S1**2
# ###########################################

# ###########################################
# Showing that numerator of a*b*c*d = -4*A*E*M4/3 - 4*A*E*M5/3 - 8*C*E/3 + B**2*E/A

# numerator of a*b*c*d = -D**2 + B*D*P1/A - B**2*P1**2/(4*A**2) + P1**2*S1**2/(4*A**2)

# replacing S1**2 with -4*A**2*M3 + B**2
# replacing P1 with -A*M3 + C
# replacing M3 with M4/3 + M5/3 + 2*C/(3*A)
# replacing M4**3 with M1/2 + M6/2
# replacing M5**3 with M1/2 - M6/2
# replacing M4**2*M5 with M2*M4
# replacing M4*M5**2 with M2*M5
# replacing M1 with 72*C*E/A**2 - 27*D**2/A**2 - 27*B**2*E/A**3 + 9*B*C*D/A**3 - 2*C**3/A**3
# replacing M2 with 12*E/A - 3*B*D/A**2 + C**2/A**2

# -4*A*E*M4/3 - 4*A*E*M5/3 - 8*C*E/3 + B**2*E/A
# ###########################################

# ###########################################
# Showing that denominator of a*b*c*d = -4*A**2*M4/3 - 4*A**2*M5/3 - 8*A*C/3 + B**2

# denominator of a*b*c*d = S1**2

# replacing S1**2 with -4*A**2*M3 + B**2
# replacing P1 with -A*M3 + C
# replacing M3 with M4/3 + M5/3 + 2*C/(3*A)

# -4*A**2*M4/3 - 4*A**2*M5/3 - 8*A*C/3 + B**2
# ###########################################

# ###########################################
# -4*A*E*M4/3 - 4*A*E*M5/3 - 8*C*E/3 + B**2*E/A    /    -4*A**2*M4/3 - 4*A**2*M5/3 - 8*A*C/3 + B**2     = 

# E/A
# ###########################################

# ###########################################
# Hence the four solutions are:

# (-B + S1 - sqrt(-4*A*(4*A*D + P1*(-2*B + 2*S1))/S1 + (-B + S1)**2))/(4*A)
# (-B + S1 + sqrt(-4*A*(4*A*D + P1*(-2*B + 2*S1))/S1 + (-B + S1)**2))/(4*A)
# (-B - S1 - sqrt(4*A*(4*A*D + P1*(-2*B - 2*S1))/S1 + (-B - S1)**2))/(4*A)
# (-B - S1 + sqrt(4*A*(4*A*D + P1*(-2*B - 2*S1))/S1 + (-B - S1)**2))/(4*A)
# ###########################################

# ###########################################
# Definitions

# S1 = sqrt(-4*A**2*M3 + B**2)
# P1 = -A*M3 + C
# M3 = M4/3 + M5/3 + 2*C/(3*A)
# M4 = (M1/2 + M6/2)**(1/3)
# M5 = (M1/2 - M6/2)**(1/3)
# M6 = sqrt(M1**2 - 4*M2**3)
# M1 = 72*C*E/A**2 - 27*D**2/A**2 - 27*B**2*E/A**3 + 9*B*C*D/A**3 - 2*C**3/A**3
# M2 = 12*E/A - 3*B*D/A**2 + C**2/A**2