def cube(x):
    return x ** 3

def process_list(func, num_list):
    return [func(num) for num in num_list]
numbers = [1, 2, 3, 4]
print("Cubes:", process_list(cube, numbers))
"""
output:
Cubes: [1, 8, 27, 64]
"""
