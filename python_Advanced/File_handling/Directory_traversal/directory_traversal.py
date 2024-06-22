import os


files = {}
directory = '../'

for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        ext = element.split('.')[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = el.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open(os.path.join(directory, 'report.txt'), 'w') as ouput_file:
    for ext, file_names in sorted(files.items()):
        ouput_file.write(f".{ext}\n")
        for file_name in sorted(file_names):
            ouput_file.write(f"- - - {file_name}\n")
