from decimal import Decimal, getcontext
from random import randint
from RootCalculator import c_square_root, c_cube_root

def FourthPoly(A: Decimal, B: Decimal, C: Decimal, D: Decimal, E: Decimal, rec_real: Decimal, rec_imag: Decimal):
    if A == 0:
        print("A can't be zero\naborting")
        print(1/0)
    else:
        # (P1 + √(P1**2 - 8aR1))/4a


        # definitions
        # P1 = (-b + S3) completed
        # R1 = (c - M3 + S4) completed

        # S3 = √(b**2 - 4aM3) completed
        # S4 = √((c - M3)**2 - 4ae) completed
        # M3 = 2c/(3) + M4/3 + M5/3 completed
        # M4 = cube_root((M1 + M6)/2) completed
        # M5 = cube_root((M1 - M6)/2) completed
        # M6 = √(M1**2 - 4M2^3) completed
        # M1 = (72ace - 27add - 27bbe + 9bcd - 2ccc) completed
        # M2 = (12ae - 3bd + cc) completed

        M1 = (72*A*C*E - 27*A*D*D - 27*B*B*E + 9*B*C*D - 2*C*C*C)
        M2 = (12*A*E - 3*B*D + C*C)

        inptu = M1*M1 - 4*M2*M2*M2
        M6_real, M6_imag = c_square_root(inptu, Decimal("0"))

        # if abs(M6_real**2 - M6_imag**2 - inptu) >  abs(rec_real):
        #     rec_real = M6_real**2 - M6_imag**2 - inptu
        #     print(f"Error {rec_real}")
        #     # print(f"Square_root {M6_real} {M6_imag}")
        #     # print(f"Output_Squared {M6_real**2 - M6_imag**2}")
        #     # print(f"Input {inptu}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        if M6_imag == 0:
            input_imag = Decimal("0")
        else:
            input_imag = -M6_imag/Decimal(2)
        input_real = (M1  - M6_real)/Decimal(2)
        M5_real, M5_imag = c_cube_root(input_real, input_imag)

        # if abs(M5_real**3 - 3*M5_real*M5_imag**2 - input_real) > rec_real:
        #     rec_real = abs(M5_real**3 - 3*M5_real*M5_imag**2 - input_real)
        #     # print(f"Cube_root {M5_real} {M5_imag}")
        #     # print(f"Output_Cubed {M5_real**3 - 3*M5_real*M5_imag**2}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {M5_real**3 - 3*M5_real*M5_imag**2 - input_real}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        # if abs(3*M5_real**2*M5_imag - M5_imag**3 - input_imag) > rec_imag:
        #     rec_imag = abs(3*M5_real**2*M5_imag - M5_imag**3 - input_imag)
        #     # print(f"Cube_root {M5_real} {M5_imag}")
        #     # print(f"Output_Cubed {M5_real**3 - 3*M5_real*M5_imag**2} {3*M5_real**2*M5_imag - M5_imag**3}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {3*M5_real**2*M5_imag - M5_imag**3 - input_imag}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")


        if M6_imag == 0:
            input_imag = Decimal("0")
        else:
            input_imag = M6_imag/Decimal(2)
        input_real = (M1  + M6_real)/Decimal(2)
        M4_real, M4_imag = c_cube_root(input_real, input_imag)

        # if abs(M4_real**3 - 3*M4_real*M4_imag**2 - input_real) > rec_real:
        #     rec_real = abs(M4_real**3 - 3*M4_real*M4_imag**2 - input_real)
        #     # print(f"Cube_root {M4_real} {M4_imag}")
        #     # print(f"Output_Cubed {M4_real**3 - 3*M4_real*M4_imag**2}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {M4_real**3 - 3*M4_real*M4_imag**2 - input_real}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        # if abs(3*M4_real**2*M4_imag - M4_imag**3 - input_imag) > rec_imag:
        #     rec_imag = abs(3*M4_real**2*M4_imag - M4_imag**3 - input_imag)
        #     # print(f"Cube_root {M4_real} {M4_imag}")
        #     # print(f"Output_Cubed {M4_real**3 - 3*M4_real*M4_imag**2} {3*M4_real**2*M4_imag - M4_imag**3}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {3*M4_real**2*M4_imag - M4_imag**3 - input_imag}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        M3_real = Decimal(2*C/3 + Decimal(M4_real/3) + Decimal(M5_real/3))
        M3_imag = Decimal(M4_imag/3 + M5_imag/3)
        
        # S4 = √((c - M3)**2 - 4ae)
        input_real = C*C - 2*C*M3_real + M3_real*M3_real - M3_imag*M3_imag - 4*A*E
        input_imag = -2*C*M3_imag + 2*M3_real*M3_imag


        if abs(input_imag) < Decimal("1e-25"):
            input_imag = Decimal("0")
        
        S4_real, S4_imag = c_square_root(input_real, input_imag)

        # if abs(S4_real**2 - S4_imag**2 - input_real) > rec_real:
        #     rec_real = abs(S4_real**2 - S4_imag**2 - input_real)
        #     # print(f"Square_root {S4_real} {S4_imag}")
        #     # print(f"Output_Squared {S4_real**2 - S4_imag**2}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {S4_real**2 - S4_imag**2 - input_real}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")
        
        # if abs(2*S4_real*S4_imag - input_imag) > rec_imag:
        #     rec_imag = abs(2*S4_real*S4_imag - input_imag)
        #     # print(f"Square_root {S4_real} {S4_imag}")
        #     # print(f"Output_Squared {S4_real**2 - S4_imag**2} {2*S4_real*S4_imag}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {2*S4_real*S4_imag - input_imag}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        # S3 = √(b**2 - 4aM3)
        input_real = B*B - 4*A*M3_real
        input_imag = -4*A*M3_imag

        if abs(input_imag) < Decimal("1e-25"):
            input_imag = Decimal("0")

        S3_real, S3_imag = c_square_root(input_real, input_imag)

        # if abs(S3_real**2 - S3_imag**2 - input_real) > rec_real:
        #     rec_real = abs(S3_real**2 - S3_imag**2 - input_real)
        #     # print(f"Square_root {S3_real} {S3_imag}")
        #     # print(f"Output_Squared {S3_real**2 - S3_imag**2} {2*S3_real*S3_imag}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {S3_real**2 - S3_imag**2 - input_real}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        # if abs(2*S3_real*S3_imag - input_imag) > rec_imag:
        #     rec_imag = abs(2*S3_real*S3_imag - input_imag)
        #     # print(f"Square_root {S3_real} {S3_imag}")
        #     # print(f"Output_Squared {S3_real**2 - S3_imag**2} {2*S3_real*S3_imag}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {2*S3_real*S3_imag - input_imag}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        # P1 = (-b + S3)
        # R1 = (c - M3 + S4)

        P1_real = Decimal(-B + S3_real)
        P1_imag = S3_imag

        R1_real = Decimal(C - M3_real + S4_real)
        R1_imag = Decimal(-M3_imag + S4_imag)

        # (P1 + √(P1**2 - 8aR1))/4a

        input_real = P1_real*P1_real - P1_imag**2 - 8*A*R1_real
        input_imag = 2*P1_real*P1_imag - 8*A*R1_imag
        if abs(input_imag) < Decimal("1e-25"):
            input_imag = Decimal("0")

        S1_real, S1_imag = c_square_root(input_real, input_imag)

        # if abs(S1_real**2 - S1_imag**2 - input_real) > rec_real:
        #     rec_real = abs(S1_real**2 - S1_imag**2 - input_real)
        #     # print(f"Square_root {S1_real} {S1_imag}")
        #     # print(f"Output_Squared {S1_real**2 - S1_imag**2} {2*S1_real*S1_imag}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {S1_real**2 - S1_imag**2 - input_real}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        # if abs(2*S1_real*S1_imag - input_imag) > rec_imag:
        #     rec_imag = abs(2*S1_real*S1_imag - input_imag)
        #     # print(f"Square_root {S1_real} {S1_imag}")
        #     # print(f"Output_Squared {S1_real**2 - S1_imag**2} {2*S1_real*S1_imag}")
        #     # print(f"Input {input_real} {input_imag}")
        #     print(f"Error {2*S1_real*S1_imag - input_imag}")
        #     print(f"quartic coefs {A} {B} {C} {D} {E}")

        # (P1 + √(P1**2 - 8aR1))/4a
        Solution_real = (S1_real + P1_real)/(4*A)
        Solution_imag = (S1_imag + P1_imag)/(4*A)
        print(f"Quartic equation with coefficients {A} {B} {C} {D} {E} has solution {Solution_real} + {Solution_imag}i")

        print("Testing")


        print()
        a, b = Solution_real, Solution_imag
        print(f"f(a + bi) = {A*(a**4 - 6*a**2*b**2 + b**4) + B*(a**3 - 3*a*b**2) + C*(a**2 - b**2) + D*a + E} + {A*(4*a**3*b - 4*a*b**3) + B*(3*a**2*b - b**3) + C*(2*a*b) + D*b}*i")
        
        print()
        a, b = Solution_real, -Solution_imag
        print(f"f(a - bi) = {A*(a**4 - 6*a**2*b**2 + b**4) + B*(a**3 - 3*a*b**2) + C*(a**2 - b**2) + D*a + E} + {A*(4*a**3*b - 4*a*b**3) + B*(3*a**2*b - b**3) + C*(2*a*b) + D*b}*i")

        print()
        a, b = -Solution_real, Solution_imag
        print(f"f(-a + bi) = {A*(a**4 - 6*a**2*b**2 + b**4) + B*(a**3 - 3*a*b**2) + C*(a**2 - b**2) + D*a + E} + {A*(4*a**3*b - 4*a*b**3) + B*(3*a**2*b - b**3) + C*(2*a*b) + D*b}*i")

        print()
        a, b = -Solution_real, -Solution_imag
        print(f"f(-a - bi) = {A*(a**4 - 6*a**2*b**2 + b**4) + B*(a**3 - 3*a*b**2) + C*(a**2 - b**2) + D*a + E} + {A*(4*a**3*b - 4*a*b**3) + B*(3*a**2*b - b**3) + C*(2*a*b) + D*b}*i")

        print(f"Total error: {rec_real} + {rec_imag}*i")
        return rec_real, rec_imag

rec_real = Decimal("0")
rec_imag = Decimal("0")
rang = 1
Ea, Eb, Ec, Ed, Ee = 5, -9, 0, -6, 8
for i in range(rang):
    a = Decimal(randint(-10, 10))
    if a == 0:
        a = Decimal("1")
    b = Decimal(randint(-10, 10))
    c = Decimal(randint(-10, 10))
    d = Decimal(randint(-10, 10))
    e = Decimal(randint(-10, 10))
    if rang == -1:
        a,b,c,d,e = Decimal(Ea), Decimal(Eb), Decimal(Ec), Decimal(Ed), Decimal(Ee)
    rec_real, rec_imag = FourthPoly(a, b, c, d, e, rec_real, rec_imag)
    
print(rec_real, rec_imag)