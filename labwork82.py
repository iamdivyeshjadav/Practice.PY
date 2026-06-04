matrix = [
    [15, 2, 39],
    [44, 5, 6],
    [7, 8, 91]
]
maximum = max(max(row) for row in matrix)
minimum = min(min(row) for row in matrix)

print("Maximum:", maximum)
print("Minimum:", minimum)
'''
Output:
Maximum: 91
Minimum: 2
'''