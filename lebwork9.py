a=int (input("enter the first number: "))
b=int (input("Enter the second number:"))
c=int (input("Enter the thaird number:"))
if a==b and b==c:
    print("All numbers are equal: ")
    if a<b:
        if a<c:
            print("The minimum number is a: ",a)
        else:
            print("The minimum number is c: ",c)
    else:
        if b<c:
            print("The minimum number is b: ",b)
        else:
            print("The minimum number is c: ",c)
else:
    if a<b:
        if a<c:
            print("The minimum number is a: ",a)
        else:
            print("The minimum number is c: ",c)
    else:
        if b<c:
            print("The minimum number is b: ",b)
        else:
            print("The minimum number is c: ",c)
'''
output:
1=> Enter the first number: 5
    Enter the second number: 10
    Enter the third number: 15
    The minimum number is a:  5
2=> Enter the first number: 20
    Enter the second number: 10
    Enter the third number: 5
    The minimum number is c:  5
3=> Enter the first number: 7
    Enter the second number: 7
    Enter the third number: 7
    All numbers are equal:  7 
'''        