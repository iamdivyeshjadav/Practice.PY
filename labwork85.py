dict_list = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_list = sorted(dict_list, key=lambda x: x["age"])
print("Sorted list of dictionaries by age:")
for item in sorted_list:
    print(item)
'''
Output:
Sorted list of dictionaries by age:
{'name': 'Bob', 'age': 25}
{'name': 'Alice', 'age': 30}
{'name': 'Charlie', 'age': 35}
'''