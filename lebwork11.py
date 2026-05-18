a=input("Enter + for addition, - for subtraction, * for multiplication, / for division: ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
if a=='+':
    print("The result is: ",num1+num2)
elif a=='-':
    print("The result is: ",num1-num2)
elif a=='*':
    print("The result is: ",num1*num2)
elif a=='/':
    if num2==0:
        print("Error: Cannot divide by zero")
    else:
        print("The result is: ",num1/num2)
else:
    print("Invalid operation! Please use +, -, *, or /")
'''
output:
1=> Enter + for addition, - for subtraction, * for multiplication, / for division: +
    Enter the first number: 5
    Enter the second number: 10
    The result is:  15.0
2=> Enter + for addition, - for subtraction, * for multiplication, / for division: -
    Enter the first number: 20
    Enter the second number: 10
    The result is:  10.0            
3=> Enter + for addition, - for subtraction, * for multiplication, / for division: *    
    Enter the first number: 7
    Enter the second number: 3
    The result is:  21.0        
4=> Enter + for addition, - for subtraction, * for multiplication, / for division: /
    Enter the first number: 10
    Enter the second number: 0
    Error: Cannot divide by zero    
5=> Enter + for addition, - for subtraction, * for multiplication, / for division: /
    Enter the first number: 10
    Enter the second number: 2
    The result is:  5.0
6=> Enter + for addition, - for subtraction, * for multiplication, / for division: ^
    Enter the first number: 10
    Enter the second number: 2
    Invalid operation! Please use +, -, *, or /    
'''