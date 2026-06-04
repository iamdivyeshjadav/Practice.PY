sample_list = [3, 1, 4, 1, 5, 9]
print("Original:", sample_list)
new_list = sorted(sample_list)
print("Using sorted():", new_list)
print("Original remains unchanged:", sample_list)
sample_list.sort()
print("Using sort():", sample_list)
'''
Output:
Original: [3, 1, 4, 1, 5, 9]
Using sorted(): [1, 1, 3, 4, 5, 9]
Original remains unchanged: [3, 1, 4, 1, 5, 9]
Using sort(): [1, 1, 3, 4, 5, 9]
'''