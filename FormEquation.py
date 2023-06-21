import sympy
import re

class main(object):
    def __init__(self, degree):
        self.degree = degree
        self.root = sympy.symbols("r")
        self.symbols = []
        for i in range(degree):
            self.symbols.append(sympy.symbols("s" + str(i)))

    def output(self, file):
        handle = open(file, 'a')
        x = 0
        handle.write("import sympy\n")
        for i in self.symbols:
            handle.write(f"{i} = 0\n")
            x += i*self.root**(self.symbols.index(i)/self.degree)
        handle.write(f"r = 0\n")
        handle.write(f"x = {x}\n")
        handle.close()

    def getSympyExpr(self):
        x = 0
        for i in self.symbols:
            x += i*self.root**(self.symbols.index(i))
        return x


