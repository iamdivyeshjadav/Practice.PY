a=int(input("enter a year: "))
b=int(input("enter another year: "))
while a<=b:
    if a%4==0:
        print(a,end=" ")
    a=a+1
"""
output:
enter a year: 2000
enter another year: 2020
2000 2004 2008 2012 2016 2020
"""