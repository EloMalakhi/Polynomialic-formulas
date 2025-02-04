import math, argparse

parser = argparse.ArgumentParser(description="Get some coefficients for a quartic equation.\nThe correct syntax is pythonV.0 ThisScript A B C D E -t")
parser.add_argument("a", metavar='N', type=float, help="The coefficient of x^4.")
parser.add_argument("b", metavar='N', type=float, help="The coefficient of x^3.")
parser.add_argument("c", metavar='N', type=float, help="The coefficient of x^2.")
parser.add_argument("d", metavar='N', type=float, help="The coefficient of x.")
parser.add_argument("e", metavar='N', type=float, help="The constant term.")
parser.add_argument("--test", action='store_true', help="Enables script to test solution")
parser.add_argument("--no-test", action='store_false', dest='test', help="Disables script to test solution")
args = parser.parse_args()

# get some coefficients from the command line
A, B, C, D, E = args.a, args.b, args.c, args.d, args.e

# f(a + bi) = X(a, b) + Y(a, b)i
def X(a, b):
    return A*(a**4 + -6*a**2*b**2 + b**4) + B*(a**3 - 3*a*b**2) + C*(a**2 - b**2) + D*a + E

def Y(a, b):
    return A*(4*a**3*b - 4*a*b**3) + B*(3*a**2*b - b**3) + C*(2*a*b) + D*b


# Proximity gives the distance from the output plotted on a coordinate system to 0, 0
# used to indicate closeness to the desired output. Zilch!
def Proximity(a, b):
    return X(a, b)**2 + Y(a, b)**2

# figures out one digit of the first solution pair
def OneDigitAtATime(cx, cy, decimal_place):
    Dict = {}
    Relevance = []
    for i in range(-5, 6):
        y_change = round(i/(10**decimal_place), decimal_place)
        for j in range(-5, 6):
            x_change = round(j/(10**decimal_place), decimal_place)
            inst_x, inst_y = round(cx + x_change, decimal_place), round(cy + y_change, decimal_place)
            Dict[Proximity(inst_x, inst_y)] = (inst_x, inst_y) # ties values to their proximity
            Relevance.append(Proximity(inst_x, inst_y))
    Relevance.sort() # makes a list of all guesses and sorts them
    return Dict[Relevance[0]]

# final test to demonstrate the correctness of the solutions
def Test(cx, cy, c2x, c2y):
    A, B, C, D, E = 1,1,1,1,1
    print(f"B/A = {B/A}") # -sol1 - sol2 - sol3 - sol4
    print(f"Mechanism of B/A with 4 solutions gives {-2*cx - 2*c2x}\n")
    print(f"C/A = {C/A}") # (sol1 + sol2)(sol3 + sol4) + sol1*sol2 + sol3*sol4
    print(f"Mechanism of C/A with 4 solutions gives {4*cx*c2x + cx**2 + cy**2 + c2x**2 + c2y**2}\n")
    print(f"D/A = {D/A}")  # -sol1*sol2(sol3 + sol4) - sol3*sol4(sol1 + sol2)
    print(f"Mechanism of D/A with 4 solutions gives {-(c2x**2 + c2y**2)*(2*cx) - (cx**2 + cy**2)*(2*c2x)}\n")
    print(f"E/A = {E/A}") # sol1 * sol2 * sol3 * sol4
    print(f"Mechanism of E/A with 4 solutions gives {(cx**2 + cy**2)*(c2x**2 + c2y**2)}\n")

cx, cy = 0, 0
for i in range(5):
    cx, cy = OneDigitAtATime(cx, cy, i)


# get the second solution pair
c2x = round(-B/2/A - cx, 4)
c2y = abs(E/A/(cx**2 + cy**2) - c2x**2)
c2y = round(math.sqrt(c2y), 4)
print(f"First solution pair = {cx}, ± {cy}*I")
print(f"Second solution pair = {c2x}, ± {c2y}*I")

# Do the final test
if args.test:
    if not args.test == "False":
        Test(cx, cy, c2x, c2y)
