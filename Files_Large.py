# Large File objects
# This is effiecient because it's not reading in all of the contents of our file all at once so it's not a memory issue


with open('test.txt', 'r') as f:
    
    for line in f:
        print(line, end='')