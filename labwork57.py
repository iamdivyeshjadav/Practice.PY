def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
describe_person(name="John", age=25, city="New York")
"""
output:
Name: John
Age: 25
City: New York
"""