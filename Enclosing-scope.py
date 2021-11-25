'''
LEGB
Local, Enclosing, Global, Built-in
'''

# The Enclosing scope has to do with nested functions. Example a function within a function

x = 'global x'

def outer():
    # x = 'outer x'
    
    def inner():
        #  nonlocal x # This will allow us to work with the local variables of enclosing functions. Can be useful in order to change the state of closures and decorators and things like that
        #  x = 'inner x'   
         print(x) # This would look in the local scope of this "enclosing" functions so 'inner x' would print first
        
    inner()
    print(x)
    
outer()
print(x)
