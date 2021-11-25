import os

print(os.getcwd())

# To navigate to a different path "chdir" stands for change directory

os.chdir('/Users/Python/Desktop')

# list directory in cwd by default. You can also add a path
print(os.listdir())

# To create a new folder

# Option #1
# os.mkdir('Os-Demo-2')

# Option #2 If you want to make directories that are a few levels deep use this Best to just use this one
# os.makedirs('Os-Demo-2/Sub-Dir-1')

# To delete directory

# Option #1 Best to use this one as it is safer
# os.rmdir('Os-Demo-2')

# Option #2 If you want to remove directories that are a few levels deep use this More dangerours
# os.removedirs('Os-Demo-2/Sub-Dir-1')


# To rename a file 

# os.rename('test.txt', 'demo.txt')
# print(os.listdir())



