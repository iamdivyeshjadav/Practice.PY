class a:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return a(self.x + other.x)

    def __str__(self):
        return str(self.x)
obj1 = a(5)
obj2 = a(10)
result = obj1 + obj2
print("Result of addition:", result)
'''
Output:
Result of addition: 15
'''