number=[10,20,30,40,50]
print("The third item:", number[2])
try:
    number[1]=25
except TypeError as e:
    print("Error:", e)
'''
output:
The third item: 30
Error: 'tuple' object does not support item assignment
'''
