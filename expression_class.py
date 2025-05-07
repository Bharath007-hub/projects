class EquationSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        result = (self.a + self.b) * self.c
        return result


a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

solver = EquationSolver(a, b, c)

print("Result of (a + b) * c is:", solver.calculate())
