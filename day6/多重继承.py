# 多重继承
class displayer:
    def test(self):
        print('显示器 test')

    def demo(self):
        print('显示器 demo')


class computer:
    def test(self):
        print('主机 test')

    def demo(self):
        print('主机 demo')


class pc(displayer, computer):
    def test(self):
        print('电脑 test')

if __name__ == '__main__':
    diannao =pc()
    diannao.test()
    print(pc.__mro__)