import sympy as sp


class GeometricObject:

    def __init__(self, label=None):
        if label is not None:
            self.label = label
        else:
            self.label = id(self)


class Point(GeometricObject):

    def __init__(self, label=None):
        super().__init__(label)
        self.x, self.y = sp.symbols(f"x({self.label}) y({self.label})")
        self.coordinates = (self.x, self.y)


class Line(GeometricObject):

    def __init__(self, label=None):
        super().__init__(label)
        self.phi, self.rho = sp.symbols(f"phi({self.label}) rho({self.label})")
        self.coordinates = (self.phi, self.rho)
