def factorial(n):
    if n < 0:
        return "Error: Negative input"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
"""
output:
120
"""