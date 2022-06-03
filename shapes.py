import math


class Circle:

   def __init__(self,radius):
      self.radius = radius

   def area(self): 
      A = math.pi*(self.radius*self.radius)
      return A
   
   def circumference(self):
      c = 2*math.pi*self.radius
      return c
