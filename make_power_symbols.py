import sympy

class main(object):
    def __init__(self, expr, prefix, power, root, bigR):
        self.expr = expr
        self.prefix = prefix
        self.power = power
        self.root = root
        self.bigR = bigR
        self.parts = []

    def make_symbols(self):
        for i in range(self.power):
            self.parts.append(self.expr.subs([(self.root, 0)]).subs([(self.bigR, self.root)]))
            self.expr = sympy.expand((self.expr - self.expr.subs([(self.root, 0)]))/self.root)

    def output(self, file):
        handle = open(file, 'a')
        handle.write("\n")
        for i in range(self.power):
            handle.write(f"{self.prefix}{i} = {self.parts[i]}\n")
        handle.close()