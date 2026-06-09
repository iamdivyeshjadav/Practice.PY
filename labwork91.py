class Employee:
    def _init_(self):
        self.name = "John Doe"
        print(f"Employee {self.name} initialized.")

    def _del_(self):
        print("Goodbye! The employee record has been deleted.")

emp = Employee()
del emp
'''
Output:
Employee John Doe initialized.
Goodbye! The employee record has been deleted.
'''