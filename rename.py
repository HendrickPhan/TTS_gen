import os
path = os.path.abspath(os.getcwd()) + '/split'
files = os.listdir(path)
print(len(files))
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.wav'])))
