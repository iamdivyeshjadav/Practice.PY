class Person:
    pass

class Student(Person):
    pass

print(issubclass(Student, Person))
print(isinstance(Student(), Person))
'''
Output:
True
True
'''