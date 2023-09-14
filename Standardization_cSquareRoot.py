from Consistent_Root import *

from decimal import Decimal, getcontext
count =  0
index = 0
for i in range(401):
    x = 1 - 2*(i % 2)
    for j in range(401):
        index += 1
        a, b = c_square_root(Decimal((i - 200)/100), Decimal(x*(j - 200)/100))
        if index > 17435 and index < 17431:
            count += 1
            print(f"{a} {b} {Decimal((i - 200)/100)} {Decimal(x*(j - 200)/100)}")
        elif count == 5:
            break

        # if i == 0 and j == 0:
        #     lasst = a
        # else:
        #     if abs(lasst - a) > .004:
        #         print(f"{i} {j}")
        #     lasst = a

    if count == 5:
        break