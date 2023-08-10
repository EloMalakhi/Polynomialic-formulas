import RootCalculator

from decimal import Decimal, getcontext
from random import randint

def random_coefficients():
    a, b, c, d, e = randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10)
    A = Decimal(a)
    if A == 0:
        A = Decimal(1)
    B = Decimal(b)
    C = Decimal(c)
    D = Decimal(d)
    E = Decimal(e)
    return A, B, C, D, E


def P2_sw(switch_num):
    if switch_num < 5:
        return 1
    elif switch_num > 8 or switch_num < 1:
        print(f"No combination #{switch_num} defaulting to 1")
        return 1
    else:
        return -1

def P3_sw(switch_num):
    if switch_num > 8 or switch_num < 1:
        print(f"No combination #{switch_num} defaulting to 1")
        return 1
    else:
        if (switch_num - 1) % 4 < 3:
            return 1
        else:
            return -1 
        
def P5_sw(switch_num):
    if switch_num > 8 or switch_num < 1:
        print(f"No combination #{switch_num} defaulting to 1")
        return 1
    else:
        if switch_num % 2 == 1:
            return 1
        else:
            return -1 

def calculate_solution(A, B, C, D, E, Debug=False, switch=1):
    # P2 is a square root
    # P3 is a square root
    # P5 is a square root
    # therefore there is a possibility of 8 solutions here,
    # four of them work, four don't
    # switch    P2     P3    P5
    #    1     pos    pos   pos
    #    2     pos    pos   neg
    #    3     pos    neg   pos
    #    4     pos    neg   neg
    #    5     neg    pos   pos
    #    6     neg    pos   neg
    #    7     neg    neg   pos
    #    8     neg    neg   neg

    M1 = Decimal(72*C*E/A**2 - 27*D*D/A**2 - 27*B**2*E/A**3 + 9*B*C*D/A**3 - 2*C**3/A**3)

    M2 = Decimal(12*E/A - 3*B*D/A**2 + C*C/A**2)

    M6_real, M6_imag = RootCalculator.c_square_root(M1*M1 - 4*M2*M2*M2, Decimal("0"))
    if Debug:
        print(M1*M1 - 4*M2*M2*M2, Decimal("0"))
        print(M6_real**2 - M6_imag**2)
        input()

    
    M4_real, M4_imag = RootCalculator.c_cube_root(Decimal(M1/2 + M6_real/2), Decimal(M6_imag/2))
    if Debug:
        print(Decimal(M1/2 + M6_real/2), Decimal(M6_imag/2))
        print(M4_real**3 - 3*M4_real*M4_imag**2, 3*M4_real**2*M4_imag - M4_imag**3)
        input()

    M5_real, M5_imag = RootCalculator.c_cube_root(Decimal(M1/2 - M6_real/2), Decimal(M6_imag/2))
    if Debug:
        print(Decimal(M1/2 - M6_real/2), Decimal(M6_imag/2))
        print(M5_real**3 - 3*M5_real*M5_imag**2, 3*M5_real**2*M5_imag - M5_imag**3)
        input()

    M3_real, M3_imag = Decimal(2*C/(3*A) + Decimal(M4_real/3) + Decimal(M5_real/3)), Decimal(M4_imag/3 + M5_imag/3)

    P2_real, P2_imag = RootCalculator.c_square_root(Decimal(B*B/(4*A*A) - M3_real), - M3_imag)
    P2_real, P2_imag = P2_sw(switch)*P2_real, P2_sw(switch)*P2_imag
    if Debug:
        print(Decimal(B*B/(4*A*A) - M3_real), - M3_imag)
        print(P2_real*P2_real - P2_imag*P2_imag, 2*P2_real*P2_imag)
        input()

    P1_real, P1_imag = P2_real - Decimal(B/(2*A)), P2_imag
    P4_real, P4_imag = Decimal((C/A - M3_real)/2), Decimal(- M3_imag/2)

    P5_real, P5_imag = RootCalculator.c_square_root(Decimal(P4_real*P4_real - P4_imag*P4_imag - E/A), Decimal(2*P4_real*P4_imag))
    P5_real, P5_imag = P5_sw(switch)*P5_real, P5_sw(switch)*P5_imag
    if Debug:
        print(Decimal(P4_real*P4_real - P4_imag*P4_imag - E/A), Decimal(2*P4_real*P4_imag))
        print(P5_real**2 - P5_imag**2, 2*P5_imag*P5_real)
        input()

    P3_real, P3_imag = RootCalculator.c_square_root(P1_real*P1_real - P1_imag*P1_imag - 4*P4_real - 4*P5_real, 2*P1_real*P1_imag - 4*P4_imag - 4*P5_imag)
    P3_real, P3_imag = P3_sw(switch)*P3_real, P3_sw(switch)*P3_imag
    if Debug:
        print(P1_real*P1_real - P1_imag*P1_imag - 4*P4_real - 4*P5_real, 2*P1_real*P1_imag - 4*P4_imag - 4*P5_imag)
        print(P3_real**2 - P3_imag**2, 2*P3_real*P3_imag)
        input()

    P6_real, P6_imag = Decimal((P1_real + P3_real)/2), Decimal((P1_imag + P3_imag)/2)
    return P6_real, P6_imag

def func(a, b, c, d, e, x_real, x_imag):
    
    output_real = Decimal(a*x_real**4 - 6*a*x_real**2*x_imag**2 + a*x_imag**4 + b*x_real**3 - 3*b*x_real*x_imag**2 + c*x_real**2 - c*x_imag**2 + d*x_real + e)
    output_imag = Decimal(4*a*x_real**3*x_imag - 4*a*x_real*x_imag**3 + 3*b*x_real**2*x_imag - b*x_imag**3 + 2*c*x_real*x_imag + d*x_imag)
    return output_real, output_imag


printSol = False
for i in range(30000):
    a,b,c,d,e = random_coefficients()
    x_real, x_imag = calculate_solution(a,b,c,d,e)
    test_real, test_imag = func(a,b,c,d,e,x_real,x_imag)
    
    if (abs(test_real) + abs(test_imag) >= 1e-23):
        x_real, x_imag = calculate_solution(a,b,c,d,e, switch=2)
        test_real, test_imag = func(a,b,c,d,e,x_real,x_imag)
        if printSol:
            print(f"a solution to {a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e} is:")
            print(f"{x_real} + {x_imag}i")
            print(f"The result of putting this value through the function gives:")
            print(test_real, test_imag)
    else:
        if printSol:
            print(f"a solution to {a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e} is:")
            print(f"{x_real} + {x_imag}i")
            print(f"The result of putting this value through the function gives:")
            print(test_real, test_imag)
        if (abs(test_real) + abs(test_imag)) >= 1e-23:
            print("FAILED")
            break

# 3888
# a = 57
# for i in range(a):
#     if int(a/(i+2)) == a/(i+2):
#         print(a/(i+2))
#         print(i+2)
#         break

# -17010 3888√19

# a^3 3a^2b√19 57ab^2 19b^3√19

# 19b^3 + 3*a^2*b = 3888 = 16*243 = b(19bb + 3aa)
# ll = []
# for i in range(3888):
#     if int(3888/(i+1)) == 3888/(i+1):
#         ll.append(i+1)
# for i in ll:
#     print(f"factor {i}: {1296/i - 19*i*i/3}")