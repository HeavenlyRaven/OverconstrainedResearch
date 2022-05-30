import sympy as sp
from numpy import zeros
from scipy.optimize import leastsq, fsolve


class GCP:

    def __init__(self, objects, equations):

        self.var = []
        for obj in objects:
            for c in obj.coordinates:
                self.var.append(c)
        self.num_of_var = len(self.var)
        self.num_of_eq = len(equations)

        self.system = sp.lambdify(self.var, equations, modules='numpy')
        self.__f = lambda x: self.system(*x).reshape(self.num_of_eq)

    def solve(self):

        return leastsq(self.__f, zeros(self.num_of_var))[0]

    def wcsolve(self):

        return fsolve(self.__f, zeros(self.num_of_var))
