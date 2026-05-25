set_1={1, 2, 3, 4}
set_2={3, 4, 5, 6}
union_set=set_1.union(set_2)
intersection_set=set_1.intersection(set_2)
difference_set=set_1.difference(set_2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
'''
output:
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
'''
