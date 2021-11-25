
# def hello_func(greeting, name= 'Jay'):
#     return f'{greeting}, {name}.'

# print(hello_func('Hi', 'Corey'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    

# * unpacks values of a list. ** unpacks values of a dictionary

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)