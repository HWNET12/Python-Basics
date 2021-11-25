import sys
sys.path.append('/Users/hwane123')
from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)
print(sys.path)