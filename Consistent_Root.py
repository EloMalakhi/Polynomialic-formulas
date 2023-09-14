from decimal import Decimal, getcontext # using Decimal to enhance the digit precision

# The purpose of a consistent cube root calculator,  is for a continuous function of cube  roots of complex and real numbers,
# the algorithm behind the calculator is a power series, this type of power series is by default slow when abs(power_expression)
# is close to 1, faster when abs(power_expression) is farther than 1, and impossible  when abs(powered_expression) is > 1.
# 
# So if statements are put in place so that slow or impossible scenarios are translated into inverse algorithms and then translated
# to produce the square roots, for instance there are the ranges 0 <= abs(b/a) <= .8, 
# .8 <= abs(b/a) <= 1.25, and 1.25 <= abs(b/a), if conversions aren't made within these different ranges,
# you would find that the cube root of the end of one range jumps to the beginning of another range when the transition happens,
# although both cube roots would be accurate, they wouldn't be feasible behavior-wise.

# This script converts six different ranges (useful for the algorithm) and 2 edge cases into a continuous function of cube roots,
# this also has some complex square root functions as well.

def multiply(a1: Decimal, b1: Decimal, a2: Decimal, b2: Decimal):
    return a1*a2 - b1*b2, a1*b2 + a2*b1

# Normal, Normal, Neg

def Continuity(R, I, mode):
    tipe = 1
    if tipe == 1:
        if mode == 0:
            return Decimal(0), Decimal(0)
        elif mode == 1:
            return R, I
        elif mode == 2:
            return multiply(R, I, Decimal(-.5), s_square_root(.75))
        elif mode == 3:
            return multiply(R, I, Decimal(-.5), -s_square_root(.75))
    elif tipe  ==  2:
        pass
    elif tipe == 3:
        pass



def c_cube_root(a: Decimal, b: Decimal):
    if a == 0 and b == 0:
        R, I = Decimal(0), Decimal(0)
        return R, I
    elif a == 0:
        R, I = Decimal(0), -s_cube_root(b)
        R, I = AZeroSM(R, I, b)
        return R, I
    elif b == 0:
        R, I = s_cube_root(a), Decimal(0)
        R, I = BZeroSM(R, I, a)
        return R, I
    else:
        # cube_root(a + bi) =
        # cube_root(a)*cube_root(1 + bi/a)

        R, I = c_cube_root_proper_form(a, b)
        return R, I
        

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

            # √(1+i) * √((a + bi)/(1 + i))
            # √(1+i) * √( (a + bi)(1 - i)/2)
            # √(1+i) * √( (a + b)/2 + (b - a)i/2  )
            # √((1+i)/2) * √(a + b + (b - a)i)
            # √(a+bi) = √(a/2 + s/2) + (|b|/b)√(s/2 - a/2)i
            # s = √(a^2 + b^2)
            # √((1+i)/2) = √(.25 + √(.125)) + √(√(.125) - .25)i

            # complementary square root = √(1/2 + i/2)
            # main square root = √( a + b + (b - a)i)

            # main square root = √(a+b)*power_series((b-a)i/(a+b))
            # or
            # main square root = √(bi-ai)*power_series((a+b)/(a-b))
            if abs(a+b) > abs(b-a):

                series_real, series_imag = c_square_root_series((b-a)/(a+b))
                if (a+b) < 0:
                    guess = s_square_root(Decimal((-a-b))) 
                    m_s_r_real = - guess*series_imag
                    m_s_r_imag = guess*series_real
                else:
                    guess = s_square_root(Decimal((a+b)))
                    m_s_r_real = guess*series_real
                    m_s_r_imag = guess*series_imag
            else:
                series_real, series_imag = c_square_root_series((a+b)/(a-b))
                if (b-a)  < 0:
                    guess_real, guess_imag =  s_square_root(Decimal(a/2-b/2)), -s_square_root(Decimal(a/2-b/2))
                else:
                    guess_real, guess_imag = s_square_root(Decimal(b/2-a/2)), s_square_root(Decimal(b/2-a/2))
                m_s_r_real  = series_real*guess_real - series_imag*guess_imag
                m_s_r_imag = guess_imag*series_real + guess_real*series_imag


            comp1 = s_square_root(Decimal(".125"))
            comp2 = s_square_root(comp1 + Decimal(.25))
            comp3 = s_square_root(comp1 - Decimal(.25))
            return m_s_r_real*comp2 - m_s_r_imag*comp3, m_s_r_imag*comp2 + m_s_r_real*comp3


        elif abs(b/a) > 1.25:
            if b > 0:
                # √(a+Bi) = √(Bi) * series(-ai/B)
                series_real, series_imag = c_square_root_series(-a/b)
                leader_real, leader_imag = s_square_root(Decimal(b/2)), s_square_root(Decimal(b/2))
                return leader_real*series_real - leader_imag*series_imag, leader_imag*series_real + leader_real*series_imag
            else:
                series_real, series_imag = c_square_root_series(-a/b)
                leader_real, leader_imag = s_square_root(Decimal(-b/2)), -s_square_root(Decimal(-b/2))
                return leader_imag*series_imag - leader_real*series_real, -leader_imag*series_real - leader_real*series_imag
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
        iterator = True
        i = -1
        while iterator:
            i += 1
            cn *= Decimal(1 - 3*i)/Decimal(3*(i+1))
            power *= power_expr
            if abs(cn*power) < Decimal("1e-27"):
                iterator = False
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

def c_cube_root_proper_form(a: Decimal, b: Decimal):
    # .8 ≤ |b/a| ≤ 1.25 or
    # 0 ≤ |b/a| ≤ .8 or
    # 1.25 ≤ |b/a|

    if .8 <= abs(b/a) and abs(b/a) <= 1.25:
        # cube_root(1 + bi/a) = (i - 1)*cube_root( (1 + b/a) + (b/a - 1)i )/cube_root(4)
        # cube_root( (1 + b/a) + (b/a - 1)i ) = guess*∑cn( ((1 + b/a) + (b/a - 1)i - guess^3)/guess^3 )
        Sign = int(a*abs(b/a)*Decimal(1.5)/b)
        if abs(b/a - 1) > abs(1 + b/a):
            guess = -s_cube_root(b/(4*a) - Decimal(.25))
            power_expr = (-1 - b/a)/(-1 + b/a)
            R, I = c_cube_root_series(power_expr)
            R, I = -I*guess, R*guess
        else:
            guess = s_cube_root(Decimal(.25) + b/(4*a))
            power_expr = (b/a - 1)/(1 + b/a)
            R, I = c_cube_root_series(power_expr)
            R, I = guess*R, guess*I
        R, I = multiply(R, I, Decimal(-1), Decimal(1))
        R, I = MRSM(R, I, a, b)

    elif 0 <= abs(b/a) and abs(b/a) <= .8:
        # cube_root(1 + bi/a) = c_cube_root_series(b/a)
        R, I = c_cube_root_series(b/a)
        R, I = LRSM(R, I, a, b)

    else:
        # cube_root(1 +bi/a) = guess*c_cube_root_series((-ai/b))
        # guess = -cube_root(b/a)*i
        power_expr = -a/b
        R, I = c_cube_root_series(power_expr)
        R, I = I*s_cube_root(b/a), -R*s_cube_root(b/a)
        R, I = GRSM(R, I, a, b)
        


    R, I = R*s_cube_root(a), I*s_cube_root(a)
    return R, I

def GRSM(R: Decimal, I: Decimal, a: Decimal, b: Decimal):
    # There are 3 cube roots for a number, this is selecting which one to use so that
    # there are no spikes in a succession of cube roots.
    # GRSM = Greater Range State Machine

    # making these tests I had to make sure i'm modifying each part to fit
    # therefore I wrote  configured next to them to know that I finished that part of the test

    if a < 0 and b > 0:
        return Continuity(R, I, 3)
    elif a < 0 and b < 0:
        return Continuity(R, I, 2)
    elif a > 0 and b > 0:
        return Continuity(R, I, 3)
    elif a > 0 and b < 0:
        return Continuity(R, I, 1)
    

def MRSM(R: Decimal, I: Decimal, a: Decimal, b: Decimal):
    # There are 3 cube roots for a number, this is selecting which one to use so that
    # there are no spikes in a succession of cube roots.
    # MRSM = Middle Range State Machine
    if a < 0 and b > 0:
        return Continuity(R, I, 2)
    elif a < 0 and b < 0:
        return Continuity(R, I, 3)
    elif a > 0 and b > 0:
        return Continuity(R, I, 1)
    elif a > 0 and b < 0:
        return Continuity(R, I, 3)
    
def LRSM(R: Decimal, I: Decimal, a: Decimal, b: Decimal):
    # There are 3 cube roots for a number, this is selecting which one to use so that
    # there are no spikes in a succession of cube roots.
    # LRSM = Lower Range State Machine
    if a < 0 and b > 0:
        return Continuity(R, I, 1)
    elif a < 0 and b < 0:
        return Continuity(R, I, 1)
    elif a > 0 and b > 0:
        return Continuity(R, I, 2)
    elif a > 0 and b < 0:
        return Continuity(R, I, 2)
    
def BZeroSM(R: Decimal, I: Decimal, a: Decimal):
    if a > 1:
        return Continuity(R, I, 2)
    elif a == 1:
        return Continuity(R, I, 2)
    elif a < -1:
        return Continuity(R, I, 1)
    elif a == -1:
        return Continuity(R, I, 1)
    elif a < 0:
        return Continuity(R, I, 1)
    elif a > 0:
        return Continuity(R, I, 2)

def AZeroSM(R: Decimal, I: Decimal, b: Decimal):
    if b > 1:
        return Continuity(R, I, 3)
    elif b == 1:
        return Continuity(R, I, 3)
    elif b < -1:
        return Continuity(R, I, 2)
    elif b == -1:
        return Continuity(R, I, 2)
    elif b < 0:
        return Continuity(R, I, 2)
    elif b > 0:
        return Continuity(R, I, 3)
    



def test_edge_cases():
    set_for_a = [[-1.02, -1.01, -1, -.99, -.98], [-.02, -.01, 0, .01, .02],[.98, .99, 1, 1.01, 1.02]]
    
    # this is the test for b == 0
    #   also includes the test for b == 0 and a == 0

    Dct = {}
    for i in set_for_a:
        counter = -1
        Debug = False
        DebugText = ""
        for a in i:
            b = 0
            Dct[(a, b)] = 1
            if counter == -1:
                counter += 1
                init_r, init_i = c_cube_root(Decimal(a), Decimal(b))
                DebugText = f"{init_r} {init_i} {a} {b}\n"
            else:
                going_r, going_i = c_cube_root(Decimal(a), Decimal(b))
                if ((going_r - init_r)**2 + (going_i - init_i)**2) > 1:
                    Debug = True
                init_r, init_i = going_r, going_i
                DebugText += f"{init_r} {init_i} {a} {b}\n"
        if Debug:
            print(DebugText)
            input()
            pass



    # This tests for inconsistent spikes around the range of abs(b/a) = 1.25
    for i in set_for_a:
        for a in i:
            set_for_b = []
            # setting the set for b
            for ii in range(2):
                inner_set = []
                for iii in range(5):
                    inner_set.append((2*(ii % 2) - 1)*1.25*a + (iii - 2)/100)
                set_for_b.append(inner_set)
            

            for ii in set_for_b:
                Debug = False
                DebugText = ""
                for b in ii:
                    Dct[(a, b)]    = 1
                    if DebugText == "":
                        init_r, init_i = c_cube_root(Decimal(a), Decimal(b))
                    else:
                        going_r, going_i = c_cube_root(Decimal(a), Decimal(b))
                        if ((going_r - init_r)**2 + (going_i - init_i)**2) > 1:
                            Debug = True
                        init_r, init_i = going_r, going_i
                    DebugText += f"{init_r} {init_i} {a} {b} {init_r**3 - 3*init_r*init_i**2} {3*init_r**2*init_i - init_i**3}\n"

                if Debug:
                    print(DebugText)
                    input()
                    pass

    # This tests for inconsistent spikes around the range of abs(b/a) = .8
    for i in set_for_a:
        for a in i:
            set_for_b = []
            # setting the set for b
            for ii in range(2):
                inner_set = []
                for iii in range(5):
                    inner_set.append((2*(ii % 2) - 1)*.8*a + (iii - 2)/100)
                set_for_b.append(inner_set)
            
            
            for ii in set_for_b:
                Debug = False
                DebugText = ""
                for b in ii:
                    Dct[(a, b)]    = 1
                    if DebugText == "":
                        init_r, init_i = c_cube_root(Decimal(a), Decimal(b))
                    else:
                        going_r, going_i = c_cube_root(Decimal(a), Decimal(b))
                        if ((going_r - init_r)**2 + (going_i - init_i)**2) > 1:
                            Debug = True
                        init_r, init_i = going_r, going_i
                    DebugText += f"{init_r} {init_i} {a} {b} {init_r**3 - 3*init_r*init_i**2} {3*init_r**2*init_i - init_i**3}\n"
                if Debug:
                    print(DebugText)
                    input()
                    pass

    # This tests for inconsistent spikes around the range of abs(b/a) = 0
    for i in set_for_a:
        for a in i:
            set_for_b = []
            # setting the set for b
            for ii in range(2):
                inner_set = []
                for iii in range(5):
                    inner_set.append((iii - 2)/100)
                set_for_b.append(inner_set)
            

            for ii in set_for_b:
                Debug = False
                DebugText = ""
                for b in ii:
                    Dct[(a, b)] = 1
                    if DebugText == "":
                        init_r, init_i = c_cube_root(Decimal(a), Decimal(b))
                    else:
                        going_r, going_i = c_cube_root(Decimal(a), Decimal(b))
                        if ((going_r - init_r)**2 + (going_i - init_i)**2) > 1:
                            Debug = True
                        init_r, init_i = going_r, going_i
                    DebugText += f"{init_r} {init_i} {a} {b} {init_r**3 - 3*init_r*init_i**2} {3*init_r**2*init_i - init_i**3}\n"
                if Debug:
                    print(DebugText)
                    input()
                    pass
    




