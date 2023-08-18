from decimal import Decimal, getcontext




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












