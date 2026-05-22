squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)
even_nums = [x for x in range(1, 21) if x % 2 == 0]
print("Evens:", even_nums)
words = ["hello", "WORLD", "PyThOn"]
lowercase_words = [word.lower() for word in words]
print("Lowercase:", lowercase_words)
'''
output:
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Evens: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Lowercase: ['hello', 'world', 'python']
'''