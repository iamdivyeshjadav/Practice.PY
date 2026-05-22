my_list=["A","B","C"]
my_tuple=("A","B","C")
my_list[0]="X"
print("Modified list:", my_list)
try:
    my_tuple[0]="X"
except TypeError as e:
    print("Error:", e)
'''
output:
Modified list: ['X', 'B', 'C']
Error: 'tuple' object does not support item assignment
'''
