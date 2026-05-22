fruits = "apple,banana,grapes".split(",")
print(fruits)
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)
multiline = "Line 1\nLine 2\nLine 3"
for line in multiline.splitlines():
    print(line)
'''
output:
['apple', 'banana', 'grapes']
Python is awesome
Line 1
Line 2
Line 3
'''