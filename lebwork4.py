even=int(input("Enter an even number: "))
odd=int(input("Enter an odd number: "))
if even%2==0 and odd%2!=0:
    print("You have entered an even number: ", even," and an odd number: ", odd)
else:
    print("Please enter valid even and odd numbers.")
'''
output: 
Enter an even number: 1268
Enter an odd number: 5979
You have entered an even number:  1268  and an odd number:  5979
'''
