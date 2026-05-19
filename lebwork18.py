n=int (input ("Enter a number: "))
if n<15:
    print("incorrect number")
else:
    a=15
    while a<=n:
        print(a,end=" ")
        a%=15
        a=a+15
""" 
output:
Enter a number: 100
15 30 45 60 75 90
Enter a number: 10
""" 