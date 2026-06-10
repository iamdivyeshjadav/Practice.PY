class Train:
    def travel(self):
        print("Travelling by Train")

class Plane:
    def travel(self):
        print("Travelling by Plane")

for obj in [Train(), Plane()]:
    obj.travel()
'''
Output:
Travelling by Train
Travelling by Plane
'''