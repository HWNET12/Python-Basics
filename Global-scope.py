'''
LEGB
Local, Enclosing, Global, Built
'''

# x = 'global x'

def test():
    global x # setting global function not used for the most part 
    x = 'local x'
    # print(y)
    print(x)

test()
print(x)
    