def filter_args(*args):
    strings = tuple(x for x in args if isinstance(x, str))
    numbers = tuple(x for x in args if isinstance(x, (int, float)))
    return strings, numbers
strs, nums = filter_args(1, "apple", 2.5, "banana", 3)
print("Strings:", strs)
print("Numbers:", nums)
"""
output:
Strings: ('apple', 'banana')
Numbers: (1, 2.5, 3)
"""
