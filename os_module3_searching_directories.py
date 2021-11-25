"""If we want to see the entire directory tree and files within the desktop """
import os
from datetime import datetime

os.chdir('/Users/Python/Desktop')

# os.walk is a genrator that yields a tuple of 3 values as it's walking the directory tree (the path, the directories within that path, and the files with that path)

for dirpath, dirnames, filenames in os.walk('/Users/Python/Desktop'):
    print('Current Path:', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
    print()
    
    
# Extremely useful if you can't remeember where a file is on your computer then you can search through the directories