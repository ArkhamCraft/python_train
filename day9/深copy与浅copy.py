# 深copy与浅copy
import copy


def simple_copy():
    """
    浅拷贝
    :return:
    """
    a = [1, 2, 3]
    b = copy.copy(a)
    b[0] = 10
    print(id(a), id(b))
    print(a, b)
    c = [a, b]
    print(id(c))
    print(id(c[0]), id(c[1]))
    print(c)
    print('-'*50)


def deep_copy():
    """
    深拷贝
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(a), id(b), id(c), id(d))
    a[0] = 10
    print(c,d)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


class Hero:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        self.equipment = ['A杖','魔晶']


def use_copy_own_obj():
    old_hero = Hero('蚂蚁',233)
    new_hero = copy.deepcopy(old_hero)
    new_hero.hp = 500
    new_hero.equipment.append('林肯法球')
    print(old_hero.name,old_hero.hp)
    print(new_hero.name,new_hero.hp)
    print(old_hero.equipment,new_hero.equipment)


simple_copy()
deep_copy()
use_copy_own_obj()
