'''
LEGB
Local, Enclosing, Global, Built-in
'''

import builtins

# print(dir(builtins))

# You have to be careful because in Python it is possible to overwrite built-in Functions 
# In this case we will get a TypeError because Python will find this in the Global scope before going to the built-in scope
def my_min():
    pass

m = min([5, 1, 4, 2, 3])

print(m)