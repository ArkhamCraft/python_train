# search,findall和sub

import re


def use_search():
    """
    search的使用
    :return:
    """
    ret = re.search(r'\d+', '播放量 51200，硬币 325，收藏 119')
    print(ret.group())


def use_sub():
    """
    sub的使用
    :return:
    """
    ret = re.sub(r'\d+', lambda x: str(int(x.group()) + 100), '播放量 51200')
    print(ret)

def use_findall():
    """
    findall的使用
    :return:
    """
    ret = re.findall(r'\d+', '播放量 51200，硬币 325，收藏 119')
    print(ret)
    ret = re.findall(r'\w+\s\d+', '播放量 51200，硬币 325，收藏 119')
    print(ret)


use_search()
use_sub()
use_findall()
