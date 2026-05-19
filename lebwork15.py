i=int (input("Enter a number: "))
sum=0
a=1
while a<=i:
    if a%2!=0:
        sum=sum+a
    a=a+1
print("sum of odd numbers is ",sum)
"""
output:
Enter a number: 20
sum of odd numbers is  100
"""