import sympy
import re


class main(object):
    def __init__(self, equations, variables):
        self.equations = equations
        self.variables = variables

    def output(self, file):
        handle = open(file, 'a')

        self.result = sympy.solve(self.equations, self.variables)
        equations = ""

        hold = ""
        print(self.result)
        count = 0
        for i in self.equations:
            count += 1
            equations += f"equation{count}, "
            hold += f"# {self.variables[count - 1]} = {self.result[self.variables[count - 1]]}\n"
        equations = re.sub(", $", "", equations)
        handle.write(f"\nequations = [{equations}]")
        handle.write(f"\nvariables = {self.variables}\n")
        handle.write(f"result = sympy.solve(equations, variables)\n")
        for i in self.variables:
            handle.write(f"{i} = result[{i}]\n")
        handle.write(hold)
        handle.close()
