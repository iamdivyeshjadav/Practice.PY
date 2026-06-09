class MyClass:
    def _init_(self, name):
        self.name = name
        print(f"Object {self.name} created.")

    def _del_(self):
        print(f"Object {self.name} is being deleted.")
obj1 = MyClass("A")
obj2 = MyClass("B")
del obj1
del obj2
'''
Output:
Object A created.
Object B created.
Object A is being deleted.
Object B is being deleted.
'''
