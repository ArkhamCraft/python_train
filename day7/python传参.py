# python的传参
import sys

print(type(sys.argv))
print(sys.argv)

def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('Hello')
    file.close()


write_hello(sys.argv[1])
