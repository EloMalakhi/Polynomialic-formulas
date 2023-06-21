import sympy
import re

class  main(object):
    def __init__(self, power):
        self.power = power
        self.two_d = []
        self.representing_eq = ""
        self.documentation = ""
        self.documentation2 = ""
        self.documentation3 = ""
        self.op_sym = ""

    def make_symbols_for_es(self):
        for i in range(self.power):
            self.two_d.append([])
            hold = ""
            for j in range(self.power):
                hold += f"p{i+1}_{j}, "
                self.two_d[-1].append(sympy.symbols(f"p{i+1}_{j}"))


    def make_equations(self, xform_symbols):
        self.equations = []
        self.coefficients = []
        self.most_relevant = []
        for i in range(self.power):
            self.coefficients.append(sympy.symbols(f"C{i}"))
        for i in range(self.power - 2):
            self.most_relevant.append(self.coefficients[i+2])


        for i in range(self.power - 2):
            part1 = 0
            part2 = 0
            part3 = xform_symbols[self.power - 1 - i]
            part4 = xform_symbols[1]
            for j in range(self.power - 2):
                part1 += self.coefficients[j+2]*self.two_d[j+1][self.power - 1 - i]
                part2 += self.coefficients[j+2]*self.two_d[j+1][1]
            part1 += self.two_d[self.power - 1][self.power - 1 - i]
            part2 += self.two_d[self.power - 1][1]
            self.documentation += f"# ({part1}) / ({part2}) = ({part3}) / ({part4})\n"
            self.documentation2 += f"# {part1*part4} = {part2*part3}\n"
            self.equations.append(sympy.expand(part1*part4 - part2*part3))
            self.documentation3 += f"equation{i+1} = {sympy.expand(part1*part4 - part2*part3)}\n"

        self.representing_eq = "# x**5"
        for i in range(self.power):
            self.representing_eq += f" + {self.coefficients[self.power - 1 - i]}*x**{self.power - 1 - i}"


    def output(self, file):
        handle = open(file, 'a')
        p1 = ""
        p2 = "sympy.symbols(\""
        for i in range(self.power):
            p1 += f"s{i}, C{i}, "
            p2 += f"s{i} C{i} "
        p2 = re.sub(" $", "\")", p2)
        p1 = re.sub(", $", "", p1)
        self.op_sym += f"{p1} = {p2}\n"

        for i in range(self.power - 1):
            p1 = ""
            p2 = "sympy.symbols(\""
            for j in range(self.power):
                p1 += f"p{i+2}_{j}, "
                p2 += f"p{i+2}_{j} "
            p2 = re.sub(" $", "\")", p2)
            p1 = re.sub(", $", "", p1)
            self.op_sym += f"{p1} = {p2}\n"

        to_write = ""    
        handle.write(f"\n{self.op_sym}\n")
        handle.write(f"\n{self.representing_eq} = 0\n")
        handle.write(f"\n{self.documentation}")
        handle.write(f"\n{self.documentation2}")
        handle.write(f"\n{self.documentation3}")
        handle.close()

