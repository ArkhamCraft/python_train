# 元组
def use_tuple():
    info_tuple = ("zhangsan", 18, 1.75, 'zhangsan')
    for i in info_tuple:
        print(i)
    print('-' * 50)
    print(info_tuple.index('zhangsan'))
    print(info_tuple.count('zhangsan'))
    print(len(info_tuple))
    print('-' * 50)

def use_str():
    info_tuple = ("小明", 21, 1.85)
    print("%s 年龄是 %d 身高是 %f" % info_tuple)
    info_str = "%s 年龄是 %d 身高是 %f" % info_tuple
    print(info_str)
    print(f'使用{info_tuple}')

def use_tuple_str():
    a = [1]
    print(type(a))
    b = (1,)
    print(type(b))
    for i in b:
        print(i)


# 字典
def use_dict_base():
    xiaoming_dict = {'name':'小明'}
    print(id(xiaoming_dict))
    print(xiaoming_dict['name'])
    xiaoming_dict['age'] = 18
    print(xiaoming_dict)
    xiaoming_dict['name'] = '小小明'
    print(xiaoming_dict)
    del xiaoming_dict['name']
    print(xiaoming_dict)
    print(len(xiaoming_dict))
    temp_dict = {"height": 1.75,"age": 20}
    xiaoming_dict.update(temp_dict)
    print('-' * 50)
    print(xiaoming_dict)
    xiaoming_dict.clear()
    print(xiaoming_dict)
    print('-' * 50)


def use_dict_iter():
    xiaoming_dict = {"name": "小明","qq": "123456","phone": "10086"}
    for k in xiaoming_dict:
        print(k, xiaoming_dict[k])
    print('-' * 50)
    for k, v in xiaoming_dict.items():
        print(f'健 {k},值 {v}')
    print('-' * 50)
    for k in xiaoming_dict.keys():
        print(k)
    print('-' * 50)
    for v in xiaoming_dict.values():
        print(v)
    print('-' * 50)

def use_list_dict():
    card_list = [{"name": "张三","qq": "12345","phone": "110"},
                 {"name": "李四","qq": "54321","phone": "10086"}]
    for card in card_list:
        print(card)

def use_unpack_package():
    k, v, w = (1, 2, 3)
    print(k, v, w)


# 字符串
def check_type():
    s1 = 'abc*'
    print(s1.isalnum())
    s2 = '123'
    print(s2.isdecimal())

def str_find():
    s1 = 'abcdefgcdef'
    print(s1.find('cd',4))
    s2 = s1.replace('cd','CD',1)
    print(s2)

def str_split_join():
    s1 = 'abc bcd 我很帅'
    print(s1.split())
    s2 = 'abc\nbcd\nefg'
    print(s2.splitlines())
    s3 = 'abc\r\nbcd\r\nefg'
    print(s3.splitlines(True))
    print('-' * 50)
    str_list = ['a', 'b', 'c', 'd']
    print(','.join(str_list))
    print('-' * 50)

def study_r():
    s = 'abc\r\nd'
    print(s)
    print('-' * 50)

def str_slice():
    num_str = "0123456789"
    print(num_str[2:6])
    print(num_str[2:])
    print(num_str[:6])
    print(num_str[:])
    print(num_str[::2])
    print(num_str[1::2])
    print(num_str[-1])
    print(num_str[2:-1])
    print(num_str[-2:])
    print(num_str[::-1])

def list_slice():
    my_list = list("0123456789")
    print(my_list)
    print(my_list[2:6])

def index_count():
    hello_str = "heallo hello"
    print(len(hello_str))
    print(hello_str.count("llo"))
    print(hello_str.count("abc"))
    print(hello_str.index("llo"))
    print('-' * 50)


# 集合
def use_set():
    set1 = set()
    print(type(set1))
    set2 = {1, 2, 3, 4, 5}
    fruits = {"apple", "banana", "cherry"}
    fruits.add("orange")
    print(fruits)
    fruits = {"apple", "banana", "cherry"}
    x = fruits.copy()
    print(id(x))
    print(id(fruits))
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(f'差集{z}')
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.difference_update(y)
    print(x)
    print('-' * 50)
    fruits = {"apple", "banana", "cherry"}
    fruits.discard("banana")
    print(fruits)
    print('-' * 50)
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)
    print(result)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)
    print(z)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)
    print(z)
    print('apple' in z)
    print(x - y)
    print(x | y)
    print(x & y)
    print(x ^ y)

def use_generator():
    my_tuple = tuple(x for x in range(10))
    print(my_tuple)
    my_set={x for x in 'abracadabra' if x not in 'abc'}
    print(my_set)
    print(len(my_set))

# 缺省参数
def test(name,age=6):
    print(name,age)

if __name__ == '__main__':
    use_tuple()
    use_str()
    use_tuple_str()
    use_dict_base()
    use_dict_iter()
    use_list_dict()
    use_unpack_package()
    check_type()
    str_find()
    str_split_join()
    study_r()
    str_slice()
    list_slice()
    index_count()
    use_set()
    use_generator()
    test('xiaoming')