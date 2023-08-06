from decimal import Decimal, getcontext
from random import randint
import random

def c_cube_root(a: Decimal, b: Decimal):
    if a == 0 and b == 0:
        # Short circuit the calculation
        return 0, 0
    elif a == 0:
        # Catch a divide by zero error
        return 0, -s_cube_root(b)
    elif b == 0:
        # Short circuit an zero-based calculation
        return s_cube_root(a), 0
    else:
        # cube root of a + bi = 
        # cube root of a * cube root series using (b/a) as a power expression
        if abs(b/a) <= 1.25 and abs(b/a) >= .8:
            # With b/a being  in the proximity of 1 or -1 the power series would progress
            # pretty slowly, so some different method has to be used.
            if b/a < 0:
                # this symbol in these comments will represent cube roots √
                # √(a+bi) = √(1+i) * √((a+bi)/(1+i))
                # √((a+bi)/(1+i)) = √((a+bi)(1 - i)/2)
                # √((a+bi)/(1+i)) = √((a+b)/2 + (b-a)i/2)

                # √((a+b)/2 + (b-a)i/2):
                #   guess = √((b-a)i/2)
                #   power_expr = -(a+b)i/(b-a)
                #   this same power_expr in the other condition would make a power expression too large for execution

                # √((a+b)/2 + (b-a)i/2) = guess * cube_root_series(power_expr)
                # √(a+bi) = √(1+i) * √((a+b)/2 + (b-a)i/2)
                # √(a+bi) = (-1/√2 + i/√2) * guess * cube_root_series(power_expr)
                # √(a+bi) = (-1/√2 + i/√2) * √((b-a)/2) * √i * cube_root_series(power_expr) 
                # √(a+bi) = (-1/√2 + i/√2) * √((a-b)/2)i * cube_root_series(power_expr)
                # √(a+bi) = (-1/√2 + i/√2) * √((a-b)/2)i * (series_real + series_imag*i)
                # √(a+bi) = (-1 + i) * √((a-b)/4)i * (series_real + series_imag*i)
                # √(a+bi) = (-i - 1) * √((a-b)/4) * (series_real + series_imag*i)
                # √(a+bi) = (i + 1) * √((b-a)/4) * (series_real + series_imag*i)

                # √(a+bi) = (i + 1) * (s_r + s_i*i) * √((b-a)/4)
                # √(a+bi) = ( (s_r - s_i) + (s_r + s_i)i) * √((b-a)/4)
                leader = s_cube_root((b-a)/4)
                power_expr = -(a+b)/(b-a)
                series_real, series_imag = c_cube_root_series(power_expr)
                return (series_real - series_imag) * leader, (series_real + series_imag) * leader

            else:
                # this symbol in these comments will represent cube roots √
                # √(a+bi) = √(1+i) * √((a+bi)/(1+i))
                # √((a+bi)/(1+i)) = √((a+bi)(1 - i)/2)
                # √((a+bi)/(1+i)) = √((a+b)/2 + (b-a)i/2)

                # √((a+b)/2 + (b-a)i/2):
                #   guess = √((a+b)/2)
                #   power_expr = (b-a)i/(a+b)
                #   this same power_expr in the other condition would make a power expression too large for execution

                # √((a+b)/2 + (b-a)i/2) = guess * cube_root_series(power_expr)
                # √(a+bi) = √(1+i) * √((a+b)/2 + (b-a)i/2)
                # √(a+bi) = (-1/√2 + i/√2) * guess * cube_root_series(power_expr)
                # √(a+bi) = (-1/√2 + i/√2) * √((a+b)/2) * √i * cube_root_series(power_expr) 
                # √(a+bi) = (-1/√2 + i/√2) * √((a+b)/2) * cube_root_series(power_expr)
                # √(a+bi) = (-1/√2 + i/√2) * √((a+b)/2) * (series_real + series_imag*i)

                # √(a+bi) = (-1 + i) * √((a+b)/4) * (series_real + series_imag*i)
                # √(a+bi) = (i - 1) * (s_r + s_i*i) * √((a+b)/4)
                # √(a+bi) = ( (- s_r - s_i) + (s_r - s_i)i) * √((a+b)/4)
                leader = s_cube_root((a+b)/4)
                power_expr = (b-a)/(a+b)
                series_real, series_imag = c_cube_root_series(power_expr)
                return (-series_real - series_imag) * leader, (series_real - series_imag) * leader

        elif abs(b/a) > 1.25:
            # In this case power expression spirals to infinity

            # since b is too much larger than a in comparison
            # i'll say that the cube root of a + bi =
            # the cube root of a + Bi

            # which equals:
            # cube_root_of_(Bi) * cube_root_series((a/Bi))
            # which equals

            # -cube_root_of_(B)*i*cube_root_series((a/Bi))
            series_real, series_imag = c_cube_root_series((-a/b))
            leader = - s_cube_root(b)
            return -leader*series_imag, leader*series_real
        else:
            # In this case power expression spirals to zero
            # cube_root_of_(a+bi) = 
            # cube_root_of_(a) * cube_root_series(bi/a)

            leader = s_cube_root(a)
            series_real, series_imag = c_cube_root_series((b/a))
            return leader*series_real, leader*series_imag

def s_cube_root(a: Decimal):
    if a == 0:
        return 0
    elif abs(a) <= 1:
        leader = Decimal((abs(a)/a)*Decimal(abs(a)**Decimal(1/3)))
    else:
        if a < 0:
            leader = -int(Decimal(abs(a))**(Decimal(1/3))) - 1
        else:
            leader = int(Decimal(a)**(Decimal(1/3))) + 1
    power_expr = Decimal(a)/Decimal(leader*leader*leader) - 1
    return leader * s_cube_root_series(power_expr)

def complex_conj_cube_root_series(a: Decimal, b: Decimal):
    # come up with the result for a power series for the cube root
    # having a direct complex conjugate pair

    real, imag = Decimal("1"), Decimal("0")
    cn = Decimal("1")
    power_expr_real = Decimal("1")
    power_expr_imag = Decimal("0")
    # pR + pI becomes (pR + pIi)*(a + bi) = (pR*a - pI*b) + (pR*b + pI*a)i
    for i in range(100):
        cn *= Decimal(1 - 3*i)/Decimal(3*(i+1))
        if i == 0:
            power_expr_real = Decimal(a)
            power_expr_imag = Decimal(b)
        else:
            power_expr_real = (power_expr_real*a - power_expr_imag*b)
            power_expr_imag = (power_expr_real*b + power_expr_imag*a)
        real += cn*power_expr_real
        imag += cn*power_expr_imag
        print(".01195287869099827926206264830")
        c_r = Decimal(real**3 - 3*real*imag**2)
        c_i = Decimal(3*real**2*imag - imag**3)
        print(c_i)
        input(i)
    return real, imag

def c_cube_root_series(power_expr: Decimal):
    # calculates the result of a single i value in a power series
    # in its varying stages
    if power_expr >= .8:
        print("power expression too large, stack trace is giving this function\n")
        print("problematic parameters")
        print(1/0)
    elif power_expr == 0:
        # shortcutting the calculation
        return Decimal("1"), Decimal("0")
    else:
        real = Decimal("1")
        imag = Decimal("0")
        cn = Decimal("1")
        power = Decimal("1")
        for i in range(100):
            cn *= Decimal(1 - 3*i)/Decimal(3*(i+1))
            power *= power_expr
            if (i+1)%4 == 1:
                imag += cn*power
            elif (i+1)%4 == 2:
                real -= cn*power
            elif (i+1)%4 == 3:
                imag -= cn*power
            else:
                real += cn*power

        return real, imag

def s_cube_root_series(power_expr: Decimal):
    # calculates the result of a cube root power series involving a real
    # number parameter
    if power_expr >= .8:
        print("power expression too large, stack trace is giving this function\n")
        print("problematic parameters")
        print(1/0)
    elif power_expr == 0:
        # shortcutting the calculation
        return Decimal("1")
    else:
        real = Decimal("1")
        cn = Decimal("1")
        power = Decimal("1")
        for i in range(400):
            cn *= Decimal(1 - 3*i)/Decimal(3*(i+1))
            power *= power_expr
            real += cn*power
        return real

def c_square_root(a: Decimal, b: Decimal):
    if a == 0 and b == 0:
        return Decimal("0"), Decimal("0")
    elif a == 0:
        if b > 0:
            return s_square_root(b)/s_square_root(Decimal("2")), s_square_root(b)/s_square_root(Decimal("2"))
        else:
            return -s_square_root(-b)/s_square_root(Decimal("2")), s_square_root(-b)/s_square_root(Decimal("2"))
    elif b == 0:
        if a > 0:
            return s_square_root(a), Decimal("0")
        else:
            return Decimal("0"), s_square_root(-a)
    else:
        if abs(b/a) >= .8 and abs(b/a) <= 1.25:
            # use 1.1, .46
            leader_real = Decimal("1.1")
            leader_imag = Decimal(".46")
            series_real, series_imag = complex_conj_square_root_series(Decimal((.9984*a + 1.012*b)/2.02094656 - 1), Decimal((.9984*b - 1.012*a)/2.02094656))
            return leader_real*series_real - leader_imag*series_imag, leader_imag*series_real + leader_real*series_imag
        elif abs(b/a) > 1.25:
            if b > 0:
                # √(a+Bi) = √(Bi) * series(-ai/B)
                series_real, series_imag = c_square_root_series(-a/b)
                leader_real, leader_imag = s_square_root(Decimal(b/2)), s_square_root(Decimal(b/2))
                return leader_real*series_real - leader_imag*series_imag, leader_imag*series_real + leader_real*series_imag
            else:
                series_real, series_imag = c_square_root_series(-a/b)
                leader_real, leader_imag = s_square_root(Decimal(-b/2)), -s_square_root(Decimal(-b/2))
                return leader_real*series_real - leader_imag*series_imag, leader_imag*series_real + leader_real*series_imag
        else:
            if a > 0:
                # √(a+bi) = √(a) * series(b/a)
                leader = s_square_root(a)
                series_real, series_imag = c_square_root_series(b/a)
                return leader*series_real, leader*series_imag
            else:
                leader = s_square_root(-a)
                series_real, series_imag = c_square_root_series(b/a)
                return -leader*series_imag, leader*series_real

def s_square_root(a: Decimal):
    if a < 0:
        print("Problematic parameter: " + str(a))
        print("Can't send a return value of a imaginary number")
        print("Aborting Program")
        print(1/0)
    else:
        if abs(a) < 1:
            leader = Decimal(a)**(Decimal(1/2))
            power_expr = Decimal(a)/Decimal(leader*leader) - 1
        else:
            leader = int(Decimal(a)**(Decimal(1/2))) + 1
            power_expr = Decimal(a)/Decimal(leader*leader) - 1
        return leader * s_square_root_series(power_expr)

def complex_conj_square_root_series(a: Decimal, b: Decimal):
    # come up with the result for a power series for the square root
    # having a direct complex conjugate pair

    real, imag = Decimal("1"), Decimal("0")
    cn = Decimal("1")
    power_expr_real = Decimal("1")
    power_expr_imag = Decimal("0")
    spiral_check = 0
    # pR + pI becomes (pR + pIi)*(a + bi) = (pR*a - pI*b) + (pR*b + pI*a)i
    for i in range(400):
        cn *= Decimal(1 - 2*i)/Decimal(2*(i+1))
        power_expr_real = (power_expr_real*a - power_expr_imag*b)
        power_expr_imag = (power_expr_real*b + power_expr_imag*a)
        if (power_expr_real**2 + power_expr_imag**2) > (a**2 + b**2) and spiral_check < 10:
            spiral_check += 1
        else:
            print("parameters a and b spiral outward to infinity")
            print("aborting")
            print(1/0)
        real += cn*power_expr_real
        imag += cn*power_expr_imag
    return real, imag

def c_square_root_series(power_expr: Decimal):
    # calculates the result of a single i value in a power series
    # in its varying stages
    if power_expr >= .8:
        print("power expression too large, stack trace is giving this function\n")
        print("problematic parameters")
        print(1/0)
    elif power_expr == 0:
        # shortcutting the calculation
        return Decimal("1"), Decimal("0")
    else:
        real = Decimal("1")
        imag = Decimal("0")
        cn = Decimal("1")
        power = Decimal("1")
        for i in range(400):
            cn *= Decimal(1 - 2*i)/Decimal(2*(i+1))
            power *= power_expr
            if (i+1)%4 == 1:
                imag += cn*power
            elif (i+1)%4 == 2:
                real -= cn*power
            elif (i+1)%4 == 3:
                imag -= cn*power
            else:
                real += cn*power
        return real, imag

def s_square_root_series(power_expr: Decimal):
    # calculates the result of a square root power series involving a real
    # number parameter
    if power_expr >= .8:
        print("power expression too large, stack trace is giving this function\n")
        print("problematic parameters")
        print(1/0)
    elif power_expr == 0:
        # shortcutting the calculation
        return Decimal("1")
    else:
        real = Decimal("1")
        cn = Decimal("1")
        power = Decimal("1")
        for i in range(400):
            cn *= Decimal(1 - 2*i)/Decimal(2*(i+1))
            power *= power_expr
            real += cn*power
        return real






def FourthPoly(A: Decimal, B: Decimal, C: Decimal, D: Decimal, E: Decimal, rec_real: Decimal, rec_imag: Decimal):
    if A == 0:
        print("A can't be zero\naborting")
        print(1/0)
    else:
        # m1 = 72ce/aa - 27dd/aa - 27bbe/aaa + 9bcd/aaa - 2ccc/aaa
        # m2 = 12e/a - 3bd/aa + cc/aa
        # M1 = aaa*m1
        # M2 = aa*m2
        M1 = 72*A*C*E - 27*A*D**2 - 27*B**2*E + 9*B*C*D - 2*C**3
        M2 = 12*A*E - 3*B*D + C**2
        vholder = M1*M1 - 4*M2*M2*M2
        vholder4 = Decimal("0")
        vholder2, vholder3 = c_square_root(vholder, vholder4)

        
        if vholder < 0:
            M6_real, M6_imag = Decimal("0"), vholder3/2
        elif vholder >0:
            M6_real, M6_imag = vholder2/2, Decimal("0")
        else:
            M6_real, M6_imag = Decimal("0"), Decimal("0")


        vholder = M1/2 + M6_real
        vholder2 = M6_imag

        M4_real, M4_imag = c_cube_root(vholder, vholder2)

        # if abs(M4_real*M4_real*M4_real - 3*M4_real*M4_imag*M4_imag - vholder) > abs(rec_real):
        #     rec_real = abs(M4_real*M4_real*M4_real - 3*M4_real*M4_imag*M4_imag - vholder)
        #     print(f"{A} {B} {C} {D} {E}")
        # if abs(3*M4_real*M4_real*M4_imag - M4_imag*M4_imag*M4_imag - vholder2) > abs(rec_imag):
        #     rec_imag = abs(3*M4_real*M4_real*M4_imag - M4_imag*M4_imag*M4_imag - vholder2)
        #     print(f"{A} {B} {C} {D} {E}")

        vholder = M1/2 - M6_real
        vholder2 = -M6_imag
        M5_real, M5_imag = c_cube_root(vholder, vholder2)

        # if abs(M5_real*M5_real*M5_real - 3*M5_real*M5_imag*M5_imag - vholder) > abs(rec_real):
        #     rec_real = abs(M5_real*M5_real*M5_real - 3*M5_real*M5_imag*M5_imag - vholder)
        #     print(f"{A} {B} {C} {D} {E}")
        # if abs(3*M5_real*M5_real*M5_imag - M5_imag*M5_imag*M5_imag - vholder2) > abs(rec_imag):
        #     rec_imag = abs(3*M5_real*M5_real*M5_imag - M5_imag*M5_imag*M5_imag - vholder2)
        #     print(f"{A} {B} {C} {D} {E}")

        M3_real = (2*C + M4_real + M5_real)/(3*A)
        M3_imag = (M4_imag + M5_imag)/(3*A)

        vholder = -4*A*(2*C + M4_real + M5_real)/3 + B**2
        vholder2 = -4*A*(M4_imag + M5_imag)/3
        
        S1_real, S1_imag = c_square_root(vholder, vholder2)

        # if abs(S1_real*S1_real - S1_imag*S1_imag - vholder) > abs(rec_real):
        #     rec_real = abs(S1_real*S1_real - S1_imag*S1_imag - vholder)
        #     print(f"{A} {B} {C} {D} {E}")
        # if abs(2*S1_real*S1_imag - vholder2) > abs(rec_imag):
        #     rec_imag = abs(2*S1_real*S1_imag - vholder2)
        #     print(f"{A} {B} {C} {D} {E}")

        P1_real = Decimal((C - M4_real - M5_real)/(3))
        P1_imag = Decimal((-M4_imag - M5_imag)/(3))


        C1_real, C1_imag = 2*S1_real - 2*B, 2*S1_imag 

        
        C2_real, C2_imag = C1_real*P1_real - C1_imag*P1_imag + 4*A*D, C1_imag*P1_real + C1_real*P1_imag
        C2_real, C2_imag = C2_real*-4*A, C2_imag*-4*A
        if (S1_real + S1_imag) < .00000000000001:
            print(S1_real)
            print(S1_imag)
            print(f"{A} {B} {C} {D} {E}")
            print(1/0)
        C3_real, C3_imag = (S1_real - B)*(S1_real - B) - S1_imag*S1_imag, 2*S1_imag*(S1_real - B)
        #(-B + S1 + sqrt(C2/S1 + C3)/(4*A)

        # C2*(S1_real - S1_imag)/(S1_real*S1_real + S1_imag*S1_imag)



        return rec_real, rec_imag

rec_real = Decimal("0")
rec_imag = Decimal("0")
rang = 0
for i in range(rang):
    a = Decimal(randint(-10, 10))
    if a == 0:
        a = Decimal("1")
    b = Decimal(randint(-10, 10))
    c = Decimal(randint(-10, 10))
    d = Decimal(randint(-10, 10))
    e = Decimal(randint(-10, 10))
    if rang == 1:
        a,b,c,d,e = Decimal(1), Decimal(0), Decimal(-1), Decimal(0), Decimal(9)
    rec_real, rec_imag = FourthPoly(a, b, c, d, e, rec_real, rec_imag)
    
print(rec_real, rec_imag)

import sympy
# (-B + S1 + sqrt(-4*A*(4*A*D + P1*(-2*B + 2*S1))/S1 + (-B + S1)**2))/(4*A)
# S1 = sqrt(-4*A**2*M3 + B**2)
# P1 = -A*M3 + C
# M3 = M4/3 + M5/3 + 2*C/(3*A)
# M4 = (M1/2 + M6/2)**(1/3)
# M5 = (M1/2 - M6/2)**(1/3)
# M6 = sqrt(M1**2 - 4*M2**3)
# M1 = 72*C*E/A**2 - 27*D**2/A**2 - 27*B**2*E/A**3 + 9*B*C*D/A**3 - 2*C**3/A**3
# M2 = 12*E/A - 3*B*D/A**2 + C**2/A**2


# (-B + S1 + sqrt(-4*A*(4*A*D + P1*(-2*B + 2*S1))/S1 + (-B + S1)**2))/(4*A)
# S1 = A((s1 s2) - (s3 s4))



# 4*A*D + P1*(-2*B)

# 4*A*A*[ -ab(c d) -cd(a b) (ab cd)*(a b c d)/2         ]
# 2*A*A*[ -cd(a b) cd(c d)         ]
# 2*A*A*[ (ab - cd)]

# S1 = A((s1 s2) - (s3 s4))



