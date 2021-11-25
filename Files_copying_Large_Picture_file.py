# Opening large jpg 
# In order to work with images you have to open them in binary mode meaning 
# We are going to be reading bytes instead of working with text
# All we have to do is append a "b" to our "r" and "w"

with open('tropical-palm-tree.jpg', 'rb') as rf:
    with open('tropical-palm-tree_copy.jpg', 'wb') as wf:
         for line in rf:
             wf.write(line)
      