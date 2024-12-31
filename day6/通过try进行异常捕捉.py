# 通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常
def NotSymmetricNumberError(Exception):
    print('不是对称数')

try:
    num = int(input('请输入一个整数'))
    a = str(num)
    if a == a[::-1]:
        print('是对称数')
    else:
        print('不是对称数')
except ValueError:
    print('输入的不是整数')
except  NotSymmetricNumberError as e:
    print(e)

