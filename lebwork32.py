sentence="machine learning and AI are trending"
print(f"position of 'AI': {sentence.find('AI')}")
new_sentence=sentence.replace('AI', 'Artificial Intelligence')
print(new_sentence)
data_string="data data mining and big data"
print(f"count of 'data': {data_string.count('data')}")
'''
output:
position of 'AI': 27
machine learning and Artificial Intelligence are trending
count of 'data': 3
'''
