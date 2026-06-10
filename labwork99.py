class Calculator:
    def multiply(self, a, b, c=1):
        return a * b * c

cal = Calculator()

print(cal.multiply(2, 3))
print(cal.multiply(2, 3, 4))
'''
Output:
6
24
'''