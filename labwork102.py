class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is running")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

Bike().move()
Car().move()
'''
Output:
Bike is running
Car is driving
'''