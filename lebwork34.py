text = "Hello World"
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Ends with 'World': {text.endswith('World')}")
dirty_str = "Data123#Science!"
clean_str = "".join(char for char in dirty_str if char.isalpha())
print(f"Cleaned: {clean_str}")
print(f"Python reversed: {'Python'[::-1]}")
'''
output:
Starts with 'Hello': True
Ends with 'World': True
Cleaned: DataScience
Python reversed: nohtyP
'''