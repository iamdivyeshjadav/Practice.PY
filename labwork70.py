# Given array
arr = [12, 35, 9, 56, 24, 15, 8]

print("Even numbers:")
for num in arr:
    if num % 2 == 0:
        print(num, end=" ")

print("\n\nOdd numbers:")
for num in arr:
    if num % 2 != 0:
        print(num, end=" ")
'''
Output:
Even numbers: 12 56 24 8
Odd numbers: 35 9 15
'''