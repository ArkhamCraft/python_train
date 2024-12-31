import random


def homework2():
    """
    求两个有序数字列表的公共元素
    :return:
    """
    s1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    s2 = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    result = set(s1).intersection(s2)
    print(result)


def homework3(a):
    """
    给定一个n个整型元素的列表a，其中有一个元素出现次数超过n / 2，求这个元素
    :param a:
    :param n:
    :return:
    """
    candidate = a[0]
    count = 0
    for i in a:
        if count == 0:
            candidate = i
            count = 1
        if i == candidate:
            count += 1
        else:
            count -= 1
    print(f'所求元素为{candidate}')


def homework5():
    """
    将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表
    :return:
    """
    info_tuple = (1, 2, 3)
    info_set = {4, 5, 6}
    a = list(info_tuple)
    a.extend(info_set)
    print(a)


def homework6():
    """
    在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0。
    :return:
    """
    a = [1, 2, 3, 4, 5, 6]
    a.insert(0, 7)
    a.append(0)
    print(a)


def homework7():
    """
    反转列表 [0,1,2,3,4,5,6,7]
    :return:
    """
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    b = a[::-1]
    print(b)


def homework8():
    """
    反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号。
    :return:
    """
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    b = a[::-1]
    print(b.index(5))


def homework9():
    """
    分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
    :return:
    """
    a = [True, False, 0, 1, 2]
    print(a.count(True))
    print(a.count(False))
    print(a.count(0))
    print(a.count(1))
    print(a.count(2))
    print('True的值为1,False的值为0')


def homework10():
    """
    从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
    :return:
    """
    a = [True, 1, 0, 'x', None, 'x', False, 2, True]
    while 'x' in a:
        a.remove('x')
    print(a)


def homework11():
    """
    从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素。
    :return:
    """
    a = [True, 1, 0, 'x', None, 'x', False, 2, True]
    del a[4]
    print(a)


def homework12():
    """
    删除列表中索引号为奇数（或偶数）的元素
    :return:
    """
    a = []
    for i in range(random.randint(0, 10)):
        a.append(random.randint(0, 10))
    print(f'原始列表：{a}')
    a = [a[i] for i in range(len(a)) if i % 2 == 0]
    print(f'删除后的列表:{a}')


def homework13():
    """
    清空列表中的所有元素
    :return:
    """
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a)
    a.clear()
    print(a)


def homework14():
    """
    对列表 [3,0,8,5,7] 分别做升序和降序排列
    :return:
    """
    a = [3, 0, 8, 5, 7]
    a.sort()
    print(f'升序排序为:{a}')
    c = a.sort(reverse=True)
    print(f'降序排序为:{a}')


def homework15():
    """
    将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0
    :return:
    """
    a = [3, 0, 8, 5, 7]
    for i in range(0, len(a)):
        if a[i] > 5:
            a[i] = 1
        else:
            a[i] = 0
    print(a)


def homework16():
    """
    遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号
    :return:
    """
    a = ['x', 'y', 'z']
    for i in a:
        print(a.index(i), end=' ')


def homework17():
    """
    将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表
    :return:
    """
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [a[i] for i in range(len(a)) if a[i] % 2 == 0]
    c = [a[i] for i in range(len(a)) if a[i] % 2 == 1]
    print(f'偶数组为{b}')
    print(f'奇数组为{c}')

# homework2()
# a = [1, 1, 1, 1, 1, 2, 3, 5, 9]
# homework3(a)
# homework5()
# homework6()
# homework7()
# homework8()
# homework9()
# homework10()
# homework11()
# homework12()
# homework13()
# homework14()
# homework15()
# homework16()
# homework17()
