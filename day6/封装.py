# 封装案例
class Arch:
    def __init__(self, name):
        self.name = name
        self.arrow_count = 0

    def add_arrow(self, count):
        self.arrow_count += count

    def archery(self):
        if self.arrow_count <= 0:
            print('没有箭了')
            return
        self.arrow_count -= 1
        print(f'{self.name}射出了一支箭，还剩{self.arrow_count}支箭')


class Archer:
    def __init__(self, name, bow: Arch = None):
        self.name = name
        self.bow = bow

    def shoot(self):
        if self.bow is None:
            print(f'{self.name}还没有弓')
            return
        print('发射！')
        self.bow.add_arrow(20)
        self.bow.archery()


if __name__ == '__main__':
    changgong = Arch('changgong')
    Emiya = Archer('Emiya')
    Emiya.shoot()
    Emiya.bow=changgong
    Emiya.shoot()
