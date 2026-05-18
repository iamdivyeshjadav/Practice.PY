a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a==b and b==c:
    print("All numbers are equal: ",a)
else:
    if a>b:
        if a>c:
            print("The maximum number is a: ",a)
        else:
            print("The maximum number is c: ",c)
    else:
        if b>c:
            print("The maximum number is b: ",b)
        else:
            print("The maximum number is c: ",c)
'''
output:
1=> Enter the first number: 5
    Enter the second number: 10
    Enter the third number: 15
    The maximum number is c:  15
2=> Enter the first number: 20
    Enter the second number: 10
    Enter the third number: 5
    The maximum number is a:  20
3=> Enter the first number: 7
    Enter the second number: 7
    Enter the third number: 7
    All numbers are equal:  7 
'''        
