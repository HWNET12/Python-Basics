# Writing to files


with open('test2.txt', 'a') as file:
    file.write('\nTest123')
    # goes back to the beginning and replaces not too usefull
    # file.seek(0)
    
