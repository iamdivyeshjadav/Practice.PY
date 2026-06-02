arr = [3, 5, 0, 4]
for num in arr:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
'''
output:
Factorial of 3 is 6
Factorial of 5 is 120
Factorial of 0 is 1
Factorial of 4 is 24
'''