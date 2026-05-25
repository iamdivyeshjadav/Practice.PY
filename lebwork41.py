student={'name':"divyesh", 'age':17, 'course':"AI ML and Data Science",'grade':"A"}
student['city'] = 'surat'
student['age'] = 21
del student['grade']
print(student)
for key, value in student.items():
    print(f"{key}: {value}")
'''
output:
{'name': 'divyesh', 'age': 21, 'course': 'AI ML and Data Science', 'city': 'surat'}
name: divyesh
age: 21
course: AI ML and Data Science
city: surat
'''

