from Consistent_Root import *

from decimal import Decimal, getcontext



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

    M1 = Decimal(72*A*C*E - 27*A*D*D - 27*B**2*E + 9*B*C*D - 2*C**3)

    M2 = Decimal(12*A*E - 3*B*D + C*C)

    M6_real, M6_imag = c_square_root(M1*M1 - 4*M2*M2*M2, Decimal("0"))
    if Debug:
        print(M1*M1 - 4*M2*M2*M2, Decimal("0"))
        print(M6_real**2 - M6_imag**2)
        input()

    input_r, input_i = Decimal(M1/2 + M6_real/2), Decimal(M6_imag/2)
    if abs(input_r) < 1e-26:
        input_r = Decimal(0)
    if abs(input_i) < 1e-26:
        input_i = Decimal(0)
    M4_real, M4_imag = c_cube_root(input_r, input_i)
    if Debug:
        print(input_r, input_i)
        print(M4_real**3 - 3*M4_real*M4_imag**2, 3*M4_real**2*M4_imag - M4_imag**3)
        input()

    input_r, input_i = Decimal(M1/2 - M6_real/2), Decimal(-M6_imag/2)
    if abs(input_r) <= 1e-26:
        input_r = Decimal(0)
    if abs(input_i) <= 1e-26:
        input_i = Decimal(0)

    M5_real, M5_imag = c_cube_root(input_r, input_i)
    if Debug:
        print(input_r, input_i)
        print(M5_real**3 - 3*M5_real*M5_imag**2, 3*M5_real**2*M5_imag - M5_imag**3)
        input()

    M3_real, M3_imag = Decimal(2*C/3 + Decimal(M4_real/3) + Decimal(M5_real/3)), Decimal(M4_imag/3 + M5_imag/3)
    if abs(M3_imag) < 1e-20:
        M3_imag = Decimal(0)
    input_r, input_i = Decimal(B*B - 4*A*M3_real), - 4*A*M3_imag

    if abs(input_r) < 1e-20:
        input_r = Decimal(0)
    if abs(input_i) < 1e-20:
        input_i = Decimal(0)

    P2_real, P2_imag = c_square_root(input_r, input_i)

    if Debug:
        print(input_r, input_i)
        print(P2_real*P2_real - P2_imag*P2_imag, 2*P2_real*P2_imag)
        input()

    P1_real, P1_imag = P2_real - B, P2_imag
    P4_real, P4_imag = Decimal(C - M3_real), Decimal(- M3_imag)


    input_r, input_i = Decimal(P4_real*P4_real - P4_imag*P4_imag - 4*A*E), Decimal(2*P4_real*P4_imag)
    if abs(input_r) < 1e-20:
        input_r = Decimal(0)
    if abs(input_i) < 1e-20:
        input_i = Decimal(0)
    P5_real, P5_imag = c_square_root(input_r, input_i)
    P5_real, P5_imag = P5_sw(switch)*P5_real, P5_sw(switch)*P5_imag
    if Debug:
        print(input_r, input_i)
        print(P5_real**2 - P5_imag**2, 2*P5_imag*P5_real)
        input()

    P3_real, P3_imag = c_square_root(P1_real*P1_real - P1_imag*P1_imag - 8*A*P4_real - 8*A*P5_real, 2*P1_real*P1_imag - 8*A*P4_imag - 8*A*P5_imag)
    P3_real, P3_imag = P3_sw(switch)*P3_real, P3_sw(switch)*P3_imag
    if Debug:
        print(P1_real*P1_real - P1_imag*P1_imag - 8*A*P4_real - 8*A*P5_real, 2*P1_real*P1_imag - 8*A*P4_imag - 8*A*P5_imag)
        print(P3_real**2 - P3_imag**2, 2*P3_real*P3_imag)
        input()

    P6_real, P6_imag = P1_real + P3_real, P1_imag + P3_imag
    return P6_real/(4*A), P6_imag/(4*A)

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
    for i in range(3889620):
        # stopped at 57697
        p = i
        e = p % 21 - 10
        d = (p // 21) % 21 - 10
        c = (p // 441) % 21 - 10
        b = (p // 9261) % 21 - 10
        a = (p // 194481) - 10
        if (p // 194481) - 10 > -1:
            a += 1
        a,b,c,d,e = makeDecimal(a,b,c,d,e)


        next_switch = True
        switch_n = 0
        while next_switch:
            switch_n += 1
            x_real, x_imag = calculate_solution(a,b,c,d,e,switch=switch_n)
            test_real, test_imag = func(a,b,c,d,e,x_real,x_imag)
            if (abs(test_real) + abs(test_imag) >= 1e-19) and switch_n < 8:
                #print(f"f({x_real}, {x_imag}) = {test_real}, {test_imag}")
                pass
            elif (abs(test_real) + abs(test_imag) >= 1e-19) and switch_n == 8:
                next_switch = False
                print(f"f({x_real}, {x_imag}) = {test_real}, {test_imag}")
                print(f"FAILED {a} {b} {c} {d} {e}")
                Fd = True
            else:
                next_switch  = False
                #print(f"SUCCESS {a} {b} {c} {d} {e}")
                pass
        if Fd:
            print(i)
            break

        if i % 40000 == 0:
            print(i)
        



