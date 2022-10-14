import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circ_area(self):
       return ((math.pi) * self.radius ** 2)
    def circ_circum(self):
       return (2 * (math.pi) * self.radius)
