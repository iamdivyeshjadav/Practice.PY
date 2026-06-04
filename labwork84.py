tuple_list = [(1, 50), (2, 10), (3, 40), (4, 30)]
sorted_list = sorted(tuple_list, key=lambda x: x[1])
print("Sorted list of tuples:", sorted_list)
'''
Output:
Sorted list of tuples: [(2, 10), (4, 30), (3, 40), (1, 50)]
'''
