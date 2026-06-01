def square_elements(nums):
    return [x**2 for x in nums]

numbers_list = [1, 2, 3, 4, 5]
squared_list = square_elements(numbers_list)
print(f"Original: {numbers_list}")
print(f"Squared: {squared_list}")
"""
output:
Original: [1, 2, 3, 4, 5]
Squared: [1, 4, 9, 16, 25]
"""