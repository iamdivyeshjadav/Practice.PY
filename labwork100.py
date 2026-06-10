class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

Dog().speak()
Cat().speak()
'''
Output:
Dog barks
Cat meows
'''