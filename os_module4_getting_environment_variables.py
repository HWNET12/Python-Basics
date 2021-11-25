""" To get environment variables """
import os
from datetime import datetime

print(os.chdir('/Users/Python/Desktop'))

print(os.environ.get('USERPROFILE'))

# Creating a file within our directictory

file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
print(file_path)

# to create file

with open(file_path, 'w') as file:
    file.write('Hello')

# To check if something is a file or directory:

print(os.path.isdir('/tmp/hdhfjfd'))

print(os.path.isfile('/tmp/hdhfjfd'))

# To split the root of the path and the extension
print(os.path.splitext('/Desktop/tests.txt'))

# to see everything available withing the os.path module
print((dir(os.path)))
    
