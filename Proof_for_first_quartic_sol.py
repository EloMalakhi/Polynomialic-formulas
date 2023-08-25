import sympy
a,b,c,d,e = sympy.symbols('a b c d e')
P1, P2, P3, P4, P5 = sympy.symbols('P1 P2 P3 P4 P5')
M3, M4, M5 = sympy.symbols('M3 M4 M5')

x = P1/(4*a) + P3/(4*a)
proof = sympy.expand(a*x**4 + b*x**3 + c*x**2 + d*x + e)

print("f(x) = ax**4 + bx**3 + cx**2 + dx + e")
print("")
print("x = P1/(4*a) + P3/(4*a)")
print("")
print(f"Therefore f(x) = {proof}")
print("")

Replacements = [(P3**2, P1**2 - 8*a*P4 - 8*a*P5),
                (P3**3, P1**2*P3 - 8*a*P4*P3 - 8*a*P5*P3),
                (P5**2, P4**2 - 4*a*e),
                (P1, P2 - b),
                (P2**2, b**2 - 4*a*M3),
                (P2**3, b**2*P2 - 4*a*M3*P2),
                (P4, c - M3),
                (M3, 2*c/3 + M4/3 + M5/3)]


print("enter . to see replacements")
dot = input()
if  dot == ".":
    print("f(x) is going to refer to incremental replacements in the result of f(x)")
    for i in Replacements:
        print(f"replacing {i[0]} with {i[1]}")
        proof = sympy.expand(proof.subs(i[0], i[1]))
        print(f"    f(x) = {proof}")
        input()

if dot != ".":
    for i in Replacements:
        proof = sympy.expand(proof.subs(i[0], i[1]))
    print("\n\nHere is the result of f(x) after all replacements")
    print(f"    f(x) = {proof}")

print(f"\nReplacing P3, P2, and P5 with 0")
part1 = proof.subs([(P3, 0), (P2, 0), (P5, 0)])
print(f"this is part 1: {part1}\n")

print(f"\nSubtracting part 1 and replacing P3 and P2 with 0")
part2 = proof.subs([(P3, 0), (P2, 0)]) - part1
print(f"this is part 2: {part2}")

print(f"\nSubtracting part 1 and part 2 from f(x) and replacing P3 and P5 with 0")
part3 = (sympy.expand(proof - part1 - part2)).subs([(P3, 0), (P5, 0)])
print(f"this is part 3: {part3}")

print(f"\nSubtracting part 1, part 2, and part 3 from f(x) and replacing P3 with 0")
part4 = (sympy.expand(proof - part1 - part2 - part3).subs([(P3, 0)]))
print(f"this is part 4: {part4}")

print(f"\nSubtracting part 1, part 2, part 3, and part 4 from f(x) gives")
part5 = sympy.expand(proof - part1 - part2 - part3 - part4)
print(f"{part5}")

part2 = part2.subs([(P5, 1)])
part3 = part3.subs([(P2, 1)])
part5 = part5.subs([(P3, 1)])
print(f"\nTherefore f(x) = {part1} +")
print(f"                  P5*({part2}) +")
print(f"                  P2*({part3}) +")
print(f"                  {part4} +")
print(f"                  P3*({part5})")

print(f"\nP2*P5 = ±(2ad - bc/3 + bM4/3 + bM5/3)")
print(f"The only way everything up to this point to be valid is for f(x) to be zero")
print(f"f(x) will only be zero if every part here is 0")
print(f"Every part will be zero if P2*P5 = (2ad - bc/3 + bM4/3 + bM5/3)")
print("")
print(f"But in reality if P2 is a square root of (b*b - 4*a*M3)")
print(f"and P5 is a square root of (P4*P4 - 4*a*e)")
print(f"The different square roots are seldom going to match (2ad - bc/3 + bM4/3 + bM5/3)")

print(f"The formula works in theory if P2*P5 = (2ad - bc/3 + bM4/3 + bM5/3)")
print(f"The formula works in practical application if the sign of P2*P5 correctly causes the result to be (2ad - bc/3 + bM4/3 + bM5/3)")





# if a*d*d = b*b*e:
#    P5 = 0
# if 8*a*a*d + b**3 - 4*a*b*c = 0:
#       P2 = 0
#       2ad - bc/3 + bM4/3 + bM5/3 = 0
#       P5 = √(-bd - cbb/4a + cc - 4*a*e)/2a

# else:
#     P5 = (2ad - bc/3 + bM4/3 + bM5/3)/P2
