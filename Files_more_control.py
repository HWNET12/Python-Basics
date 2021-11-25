# File Objects

with open('test.txt', 'r') as file:
   ### You can pass in how many characters in the file
    # file_contents = file.read(100)
    # print(file_contents, end='')
    
   ### If we run it again it picks up where we left off and gives us the next 100 characters
    # file_contents = file.read(100)
    # print(file_contents, end='')
   
   ### Instead of hardcoding the number of characters we can run a while loop since when we get to the end it gives us an empty string
    size_to_read = 10
    file_contents = file.read(size_to_read)
    
    # while len(file_contents) > 0:
    #     print(file_contents, end='*')
    #     file_contents = file.read(size_to_read)
    
    print(file.tell())
        
        