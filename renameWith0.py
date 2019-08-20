import os

# path = os.getcwd()
path = './data'
file_list = os.listdir(path)

for file in file_list:
    filename = file.zfill(10)
    # print(filename)
    new_name = ''.join(filename)
    os.rename(path + '\\' + file, path + '\\' + new_name)
