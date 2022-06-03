import math


class Sphere:

    def __init__(self,r):
        self.r = r

    def surface_area (self):
        SA = 4*(math.pi*self.r*self.r)
        return SA

    def volume (self):
        V = 4/3*(math.pi*self.r*self.r*self.r)
        return V

