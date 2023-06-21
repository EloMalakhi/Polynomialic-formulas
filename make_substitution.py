import sympy
import re

class main(object):
    def __init__(self: object, expr: list, dictionary: dict, power: int):
        self.dict = dictionary
        self.expressions = expr
        self.power = power

    def subst(self):
        new_expressions = []
        for i in self.expressions:
            expr = i
            for j in self.dict:
                expr = sympy.expand(expr.subs([(j, self.dict[j])]))
            new_expressions.append(expr)
        self.expressions = new_expressions

    def output(self, file, variable_extension, Variables):
        op_list = ""
        for i in range(self.power - 1):
            for j in range(self.power):
                op_list += f"                                 (p{i+2}_{j}, P{i+2}_{j}),\n"
        op_list = re.sub(",\n$", "\n", op_list)
        op_list = "    replacements.append(sympy.expand(i.subs([\n" + op_list + "                             ])))\n"


        ForContent = f"for i in [{Variables}]:"

        Test_method = ""
        for i in range(len(Variables.split(", "))):
            Test_method += f"{Variables.split(', ')[i]} = {self.expressions[i]}\n"


        handle = open(file, 'a')
        handle.write("\nreplacements = []\n")
        handle.write(f"{ForContent}\n")
        handle.write(f"{op_list}\n")
        handle.write(f"{Variables} = replacements\n")
        handle.write(Test_method)
        handle.write("# Now fill out the values yourself and test the accuracy of the operations")
        handle.close()
