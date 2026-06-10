import math


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

c = Circle(5)
r = Rectangle(4, 6)
print("Area of Circle:", c.area())
print("Area of Rectangle:", r.area())
'''
Output:
Area of Circle: 78.53981633974483
Area of Rectangle: 24
'''
