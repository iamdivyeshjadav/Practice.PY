a=input("Enter word: ")
for i in a:
    if i in "aeiouAEIOU":
        continue
    print(i,end="")
"""
output:
Enter word: Hello World
Hll Wrld
"""