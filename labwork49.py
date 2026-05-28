def frequency_analysis():
    text = "hello world"
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    print("Character Frequency:")
    for char, count in frequency.items():
        for _ in range(count):
            print(f"{char}: {count}")
frequency_analysis()
"""
output:
Character Frequency:
h: 1
e: 1
l: 3
l: 3
l: 3
o: 2
o: 2
 : 1
w: 1
r: 1
d: 1
"""
