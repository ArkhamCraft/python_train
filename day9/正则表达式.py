# 正则表达式
import re


def single():
    """
    匹配单个字符
    :return:
    """
    # 匹配任意一个字符
    ret = re.match('A.ex', 'Alex')
    print(ret.group())
    # 匹配[]中列举的字符
    ret = re.match('Hello [Pp]ython', 'Hello Python')
    print(ret.group())
    ret = re.match('[0-35-9]', '685221')
    print(ret.group())
    # 使用\d
    ret = re.match(r'今天钓了\d条鱼', '今天钓了5条鱼，可以大吃一顿了')
    print(ret.group())


def multiple():
    """
    匹配多个字符
    :return:
    """
    # *,+,?的使用
    ret = re.match(r'[A-Z][a-z]*', 'Alexisaplayer')
    print(ret.group())
    ret = re.match(r'[A-Z]*[a-z]', 'ALEx')
    print(ret.group())
    ret = re.match(r'[A-Z]?[a-z]*[0-9]+', 'Alex65536')
    print(ret.group())

    # 命名规范，只能由大小写的字母开头
    names = ['name1', '_name', '2_name', 'Name3']
    for name in names:
        ret = re.match(r'[a-zA-Z]+\w*', name)
        if ret:
            print(f'{ret.group()}是规定的命名')
        else:
            print(f'{name} 不符合命名规范')


def start_end():
    """
    邮箱问题
    :return:
    """
    email_list = ['83618484465@gmail.com',
                  'jane_smith@qq.com',
                  'user123@outlook.com',
                  '184732851216@qq.com87123']

    for email in email_list:
        ret = re.match(r'\w{4,20}@(gmail|qq|outlook)\.com$', email)
        if ret:
            print(f'{ret.group()}是正确的邮箱地址')
        else:
            print(f'{email}邮箱地址不正确')


def class_group():
    """
    网站信息问题
    :return:
    """
    website = ['<html><h1>www.cskaoyan.com</h1></html>',
               '<html><h1>www.cskaoyan.com</h2></html>']

    for website in website:
        ret = re.match(r'<(?P<web1>\w*)><(?P<web2>\w*)>.*</(?P=web2)></(?P=web1)>',website)
        if ret:
            print(f'{ret.group()}是合格的标签')
        else:
            print(f'{website}不符合要求')


single()
multiple()
start_end()
class_group()
