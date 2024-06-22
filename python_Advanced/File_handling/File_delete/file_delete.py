import os

path = os.path.join('..', 'File_writer', 'my_first_file.txt')

if os.path.exist(path):
    os.remove(path)
else:
    print('File does not exist')

