class Animal:
    def _init_(self, name):
        self.name = name

    def display_name(self):
        print(f"The animal's name is: {self.name}")

dog = Animal("Buddy")
dog.display_name()
'''
Output:
The animal's name is: Buddy
'''