class Student:
    def _init_(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name} | Roll No: {self.roll_no} | Grade: {self.grade}")
        
s1 = Student("Alice", 101, "A")
s1.display_info()
'''
Output:
Student: Alice | Roll No: 101 | Grade: A
'''