import os


def dps(current_path, width):
    file_list = os.listdir(current_path)
    for file in file_list:
        print(' '*width, file)
        new_path = current_path + '/' + file
        if os.path.isdir(new_path):
            dps(new_path, width+4)


dps('python/day7',0)