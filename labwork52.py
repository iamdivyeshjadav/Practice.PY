def char_frequency(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
print(char_frequency("hello"))
"""
output:
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""