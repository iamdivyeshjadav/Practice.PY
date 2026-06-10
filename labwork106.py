class grandparent:
    pass
class parent(grandparent):
    pass
class child(parent):
    pass
print(issubclass(child, parent))
print(issubclass(child, grandparent))
print(isinstance(child(), parent))
print(isinstance(child(), grandparent))
'''
Output:
True
True
True
True
'''
