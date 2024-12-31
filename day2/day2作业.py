def homework2():
    """
    自己定义变量赋值不同的数据类型并打印，并使用type
    :return:
    """
    # int
    i = 25
    print(i)
    print(type(i))
    f = 3.14159
    print(f)
    print(type(f))
    print(True-1)
    print(False+1)
    c = complex(2, 3)
    print("c is %d+%dj" % (c.real, c.imag))
    print("-"*50)


def homework3():
    """
    够将整型转为不同进制，进行输出
    :return:
    """
    a = 233
    print(bin(a))
    print(oct(a))
    print(hex(a))
    b = -4
    print(bin(b))
    print("-"*50)



def homework4():
    """
    1到100之间的奇数求和
    :return:
    """
    count = 0
    i = 0
    while i <= 100:
        if i % 2 == 1:
            count += i
        i += 1
    print("0~100之间的奇数求和结果 = %d" % count)
    print("-"*50)


def homework5():
    """
    九九乘法表
    :return:
    """
    # 行数
    m = 1
    while m <= 9:
        # 列数
        n = 1
        while n <= m:
            print("%d * %d = %d" % (m, n, m * n),end="\t")
            n += 1
        m += 1
        print("\n")
    print("-" * 50)


def homework6(n):
    """
    统计一个整数对应的二进制数的1的个数
    :return:
    """
    count = 0
    h = 0
    while h < 64:
        if n & 1 == 1:
            count += 1
        n = n >> 1
        h += 1
    print(count)
    print("-" * 50)




homework2()
homework3()
homework4()
homework5()
homework6(15)
