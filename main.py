import FormEquation
import assimilation
import make_power_symbols
import make_mult_s_eq
import solve_and_output
import make_substitution
import sympy
import re
import time

File = "Solving_For_Fifth.py"
# Make the equation representing x
power = 5
Fifth = FormEquation.main(power)
expr = Fifth.getSympyExpr()
Fifth.output(File)

# Make the symbols for powering x from 2 to power
dictionary = {}
for i in range(power - 1):
    radical_root_assimilation = assimilation.main(sympy.expand(expr**(i+2)), Fifth.root, power)
    radical_root_assimilation.performs_modulus()
    radical_root_breakdown = make_power_symbols.main(radical_root_assimilation.expr, 
                                                    f"P{i+2}_", 
                                                    power, 
                                                    Fifth.root, 
                                                    radical_root_assimilation.R)

    radical_root_breakdown.make_symbols()
    for j in radical_root_breakdown.parts:
        dictionary[f"p{i+2}_{radical_root_breakdown.parts.index(j)}"] = j
    radical_root_breakdown.output(File)

instance = make_mult_s_eq.main(power)
instance.make_symbols_for_es()
instance.make_equations(Fifth.symbols)
instance.output(File)

solver = solve_and_output.main(instance.equations, instance.most_relevant)
solver.output(File)

handler_list = []
for i in solver.result.values():
    handler_list.append(sympy.fraction(i)[0])
    handler_list.append(sympy.fraction(i)[1])

make_subs = make_substitution.main(handler_list, dictionary, power)

Variables = ""
Initialization = ""
for i in range(power - 2):
    Variables += f"C{i+2}_numerator, C{i+2}_denominator, "
    Initialization += f"C{i+2}_numerator, C{i+2}_denominator = sympy.fraction(C{i+2})\n"
Variables = re.sub(", $", "", Variables)



handle2 = open(File, 'a')
handle2.write(Initialization)
handle2.close()


make_subs.subst()
make_subs.output(File, "", Variables)
# instance.two_d gives the p symbols
