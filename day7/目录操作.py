# 目录的listdir，getcwd,chdir的使用
import os


def dir_func():
    file_list = os.listdir('.')
    print(file_list)
    print(os.getcwd())
    # os.mkdir('file2')
    os.chdir('file2')
    file = open('file1', 'w', encoding='utf8')
    file.close()


dir_func()