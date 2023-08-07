from decimal import Decimal, getcontext



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
            # print(leader**3*series_real**3 - 3*leader**3*series_real*series_imag**2)
            # print(3*leader**3*series_real**2*series_imag - leader**3*series_imag**3)
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










