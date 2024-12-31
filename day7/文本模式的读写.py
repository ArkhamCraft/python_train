# 文件的读写操作
def open_rw():
    file = open('file1', mode='r+', encoding='utf-8')
    text = file.read()
    print(f'读取的内容：{text}')
    file.write('happy')
    file.close()


open_rw()