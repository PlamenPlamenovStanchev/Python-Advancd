try:
    file = open('text.txt')
    print('File found')
except FileNotFoundError:
    print('File not found')


# import os
# from constants import ABSOLUTE_PROJECT_PATH
# path = path.os.join(ABSOLUTE_PROJECT_PATH, 'File_handling', 'File_penner', 'text.txt')
#
# try:
#     open(path)
#     print('File found')
# except FileNotFoundError:
#     print('File not found')