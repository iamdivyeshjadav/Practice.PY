arr = [10, 20, 30, 40, 50]
target = 40

if target in arr:
    index = arr.index(target)
    print(f"Element {target} found at index {index}")
else:
    print("Element not found")
'''
output:
Element 40 found at index 3
'''