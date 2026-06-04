matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transposed Matrix:")
for row in transposed:
    print(row)
'''
Output
Transposed Matrix:
[1, 4]
[2, 5]
[3, 6]
'''
