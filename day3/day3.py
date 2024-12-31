import module
def homework1(n):
    """
    有7个整数，其中有3个数出现了两次，1个数出现了一次， 找出出现了一次的那个数
    :return:
    """
    count = {}
    for i in n:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i, freq in count.items():
        if freq == 1:
            print(i)

def homework2():
    """
    写一个简单的for循环，从1打印到20，横着打为1排
    :return:
    """
    for i in range(21):
        if i > 0:
            print(i,end=" ")
    print()


def homework3(n):
    """
    写一个say_hello函数打印多次hello
    :return:
    """
    for i in range(n):
        print("say_hello")


def homework4(name_list):
    """
    练习列表基本使用
    :return:
    """
    print(name_list[0])
    print(name_list.index('wangwu'))
    name_list[1] = '李四'
    name_list.append('王五')
    print(name_list)
    name_list.insert(1,'王小美')
    print(name_list)
    temp_list = ["孙悟空", "猪二哥", "沙师弟"]
    name_list.extend(temp_list)
    print(name_list)
    name_list.remove('wangwu')
    print(name_list)
    name_list.pop()
    print(name_list)
    # name_list.clear()
    # print(name_list)
    name_list.append(3)
    print(name_list)
    num_list = [8,2,3,4,5,6,7,1]
    num_list.sort()
    print(num_list)
    num_list.sort(reverse=True)
    print(num_list)
    num_list.reverse()
    print(num_list)
    a = [j for i in range(10) for j in range(10)]
    print(a)
    a = [[col*row for row in range(5)] for col in range(5)]
    print(a)
    b = [j for x in a for j in x]
    print(b)
    c = [x for x in range(10)if x%2 == 0]
    print(c)
    d =[x if x%2 ==0 else x ** 2 for x in range(10)]
    print(d)


if __name__ == '__main__':
    n_list = [2, 2, 3, 3, 4, 5, 5]
    homework1(n_list)
    homework2()
# 调用函数，打印5次"say_hello"
    homework3(5)
    module.print_line1()
    module.print_line2()
    module.print_line3()
    name_list = ["zhangsan","lisi","wangwu"]
    homework4(name_list)