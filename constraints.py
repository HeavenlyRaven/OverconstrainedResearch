from objects import Point, Line
from sympy import cos, sin, pi


class Constraint:

    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def eq(self):
        pass


class ParametricConstraint(Constraint):

    def __init__(self, obj1, obj2, param):
        super().__init__(obj1, obj2)
        self.param = param


class Distance(ParametricConstraint):

    def __init__(self, obj1: Point, obj2: Point, param: float):
        super().__init__(obj1, obj2, param)

    @property
    def eq(self):
        x1 = self.obj1.x
        y1 = self.obj1.y
        x2 = self.obj2.x
        y2 = self.obj2.y
        return (x1-x2)**2 + (y1-y2)**2 - self.param**2


class Angle(ParametricConstraint):

    def __init__(self, obj1: Line, obj2: Line, param: float):
        super().__init__(obj1, obj2, param)

    @property
    def eq(self):
        phi1 = self.obj1.phi
        phi2 = self.obj2.phi
        return (phi1-phi2)**2 - (pi - self.param)**2


class Incidence(Constraint):

    def __init__(self, obj1: Point, obj2: Line):
        super().__init__(obj1, obj2)

    @property
    def eq(self):
        x = self.obj1.x
        y = self.obj1.y
        phi = self.obj2.phi
        rho = self.obj2.rho
        return x*cos(phi) + y*sin(phi) - rho


class Perpendicular(Constraint):

    def __init__(self, obj1: Line, obj2: Line):
        super().__init__(obj1, obj2)

    @property
    def eq(self):
        return Angle(self.obj1, self.obj2, pi/2).eq


class Parallel(Constraint):

    def __init__(self, obj1: Line, obj2: Line):
        super().__init__(obj1, obj2)

    @property
    def eq(self):
        phi1 = self.obj1.phi
        phi2 = self.obj2.phi
        return phi1 - phi2
