class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(f"Area of Rectangle: {rect.calculate_area()}")
'''
Output:
Area of Rectangle: 50
'''
