class Shape:
    def area(self, a, b=None):
        if b is None:
            return 3.14 * a * a      
        return a * b                

s = Shape()

print("Circle Area:", s.area(5))
print("Rectangle Area:", s.area(4, 6))
'''
Output:
Circle Area: 78.5
Rectangle Area: 24
'''