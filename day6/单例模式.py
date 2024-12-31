# 单例模式
class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    player1 = MusicPlayer('床边故事')
    player2 = MusicPlayer('夜曲')
    print(player1.name)
    print(player2.name)