from re import A, L


class Rectangle:

    def __init__(self,w,l):
        self.w = w
        self.l = l

    def area (self):
        A = (self.w*self.l)
        return A

    def perimeter (self):
        P = 2*(self.l + self.w)
        return P
