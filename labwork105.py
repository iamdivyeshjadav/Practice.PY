class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee:", self.name)

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        print("Manager Created")

m = Manager("Rahul")
'''
Output:
Employee: Rahul
Manager Created
'''