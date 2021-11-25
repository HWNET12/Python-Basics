import os
from datetime import datetime

os.chdir('/Users/Python/Desktop')

# To look at some information about our files
# print(os.stat('demo.txt'))

# st_mtime is time it was modiefied it gives you a timestanmp so you can import datetime to convert that
mod_time = os.stat('demo.txt').st_mtime
# Gives human readable time
print(datetime.fromtimestamp(mod_time))