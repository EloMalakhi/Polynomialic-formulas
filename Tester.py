from Consistent_cRoot import *

from decimal import Decimal, getcontext
from random import randint


# This function tests various things, what inputs are necessary to produce imaginary roots with negative real parts,
# the main purpose, though is to figure out under what conditions is 2ad - bc/3 + bM4/3 + bM5/3 negative or positive
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
        if (switch_num - 1) % 4 < 2:
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

def getM4(A, B, C, D, E):
    M1 = Decimal(72*A*C*E - 27*A*D*D - 27*B**2*E + 9*B*C*D - 2*C**3)

    M2 = Decimal(12*A*E - 3*B*D + C*C)

    M6_real, M6_imag =c_square_root(M1*M1 - 4*M2*M2*M2, Decimal("0"))

    input_r, input_i = Decimal(M1/2 + M6_real/2), Decimal(M6_imag/2)
    if abs(input_r) < 1e-26:
        input_r = Decimal(0)
    if abs(input_i) < 1e-26:
        input_i = Decimal(0)
    M4_real, M4_imag =c_cube_root(input_r, input_i)
    return 2*M4_real

def test_p2p5(A, B, C, D, E, Debug=False, switch=1):


    M1 = Decimal(72*A*C*E - 27*A*D*D - 27*B**2*E + 9*B*C*D - 2*C**3)

    M2 = Decimal(12*A*E - 3*B*D + C*C)

    M6_real, M6_imag =c_square_root(M1*M1 - 4*M2*M2*M2, Decimal("0"))
    if Debug:
        print(M1*M1 - 4*M2*M2*M2, Decimal("0"))
        print(M6_real**2 - M6_imag**2)
        input()

    input_r, input_i = Decimal(M1/2 + M6_real/2), Decimal(M6_imag/2)
    if abs(input_r) < 1e-26:
        input_r = Decimal(0)
    if abs(input_i) < 1e-26:
        input_i = Decimal(0)
    M4_real, M4_imag =c_cube_root(input_r, input_i)
    if Debug:
        print(input_r, input_i)
        print(M4_real**3 - 3*M4_real*M4_imag**2, 3*M4_real**2*M4_imag - M4_imag**3)
        input()

    

    if (6*A*D - B*C + 2*B*M4_real) > 0:
        return 1
    elif (6*A*D - B*C + 2*B*M4_real) == 0:
        return 0
    else:
        return -1
    # if (M4_real ) < 0:
    #     return -1
    # elif M4_real > 1:
    #     return 1
    # else:
    #     return 0

def func(a, b, c, d, e, x_real, x_imag):
    output_real = Decimal(a*x_real**4 - 6*a*x_real**2*x_imag**2 + a*x_imag**4)
    output_imag = Decimal(4*a*x_real**3*x_imag - 4*a*x_real*x_imag**3)


    output_real += Decimal(b*x_real**3 - 3*b*x_real*x_imag**2)
    output_imag += Decimal(3*b*x_real**2*x_imag - b*x_imag**3)


    output_real += Decimal(c*x_real**2 - c*x_imag**2)
    output_imag += Decimal(2*c*x_real*x_imag)


    output_real += Decimal(d*x_real)
    output_imag += Decimal(d*x_imag)


    output_real += Decimal(e)




    return output_real, output_imag


def makeDecimal(a,b,c,d,e):
    A = Decimal(a)
    if A == 0:
        A = Decimal(1)
    B = Decimal(b)
    C = Decimal(c)
    D = Decimal(d)
    E = Decimal(e)
    return A, B, C, D, E



Test = True
if Test == True:
    Fd = False
    for i in range(400):
        # stopped at 57697
        a,b,c,d,e = randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10), randint(-10, 10)
        if a == 0:
            a = 1
        a,b,c,d,e = makeDecimal(a,b,c,d,e)


        passed = test_p2p5(a,b,c,d,e)
        if passed == 1 and a*d**2 > e*b**2:
            print(f"{a} {b} {c} {d} {e}")
            print(f"{a*d*d} {b*b*e}")
            print(f"{b*c - 6*a*d}")
            M4 = getM4(a, b, c, d, e)
            print(M4)
            break
                   

        
        



