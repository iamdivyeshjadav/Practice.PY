a=int (input ("Enter first number: "))
b=int (input("Enter second number: "))
c=int (input("Enter third number: "))
d=int (input("Enter forth number: "))
if a==b and b==c and c==d :
    print ("all numbers are same:")
    if a>b:
        if a>c:
            if a>d:
                print ("the maximum number is a: ",a)
            else:
                print ("the maximum number is d: ",d)
        else:
               print ("the maximum number is c: ",c)
    else:
            if b>c:
                if b>d:
                    print ("the maximum number is b: ",b)
                else:
                    print ("the maximum number is d: ",d)
            else:
                if c>d:
                    print ("the maximum number is c: ",c)
                else:
                    print ("the maximum number is d: ",d)
else:
    if a>b:
        if a>c:
            if a>d:
                print ("the maximum number is a: ",a)
            else:
                print ("the maximum number is d: ",d)
        else:
            if c>d:
                print ("the maximum number is c: ",c)
            else:
                print ("the maximum number is d: ",d)
    else:
        if b>c:
            if b>d:
                print ("the maximum number is b: ",b)
            else:
                print ("the maximum number is d: ",d)
        else:
            if c>d:
                print ("the maximum number is c: ",c)
            else:
                print ("the maximum number is d: ",d)
''' 
output:
1=> Enter first number: 5
    Enter second number: 10
    Enter third number: 15
    Enter forth number: 20
    The maximum number is d:  20
2=> Enter first number: 20
    Enter second number: 10
    Enter third number: 5
    Enter forth number: 0
    The maximum number is a:  20
3=> Enter first number: 7
    Enter second number: 7
    Enter third number: 7
    Enter forth number: 7       
    All numbers are same:  7
'''