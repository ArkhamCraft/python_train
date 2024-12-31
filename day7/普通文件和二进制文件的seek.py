import os


def seek_start():
    file = open('file1', mode='r+', encoding='utf-8')
    file.seek(2, 0)
    text = file.read(5)
    print(text)


def seek_end():
    file = open('file1', mode='r+', encoding='utf-8')
    file.seek(0, 2)
    text = file.read(5)
    print(text)
    file.close()


def seek_b():
    file = open('file1', mode='r+')
    b = file.read(3)
    print(b)
    file.close()


seek_start()
seek_end()
seek_b()
