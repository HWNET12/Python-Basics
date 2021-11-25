# File Objects

with open('test.txt', 'r') as file:
    # file_contents = file.read()
    # To get a list of the files int the file
    file_contents_list = file.readline()
    print(file_contents_list, end='')
    
    