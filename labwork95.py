class MyClass:
    def __init__(self):
        self.value = 0

    def add(self, a, b):
        return a + b

obj = MyClass()
print(obj.add(10, 20))
print(obj.add("Hello ", "World"))
'''
Output:
30
Hello World
'''