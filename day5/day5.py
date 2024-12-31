# 缺省函数
def print_info(name, title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print(f'{name}是{title}, {gender_text}')


print_info("小明")
print_info("老王", title="班长")
print_info("小美", title="学习委员", gender=False)
print_info("小美", gender=False, title="学习委员")


# 多值参数
def demo2(*args, **kwargs):
    print(f'demo2-{args}, {kwargs}')


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
    demo2(*args, **kwargs)


demo(1, 2, 3, 4, 5, 5, 6, name='小明', age=18)


# 类
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def wwj(self):
        print(self.name + '正在汪汪叫')

    def ywb(self):
        print(self.name + '正在摇尾巴')

dahuang = Dog('大黄','黄色')
dahuang.wwj()
dahuang.ywb()
