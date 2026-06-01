def print_students(*args):
    if not args:
        print("No student names provided.")
        return
    for name in args:
        print(name)
print_students("Alice", "Bob", "Charlie")
print_students()  
"""
output:
Alice
Bob
Charlie
No student names provided.
"""
