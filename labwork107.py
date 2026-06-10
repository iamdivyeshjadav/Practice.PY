class Base:
    def display(self):
        print("This is Base class method")

class Derived(Base):
    def display(self):
        super().display()
        print("This is Derived class method")

obj = Derived()
obj.display()
'''
Output:
This is Base class method
This is Derived class method
'''