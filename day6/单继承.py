# 单继承
class player:
    def jump(self):
        print('跳')

    def squat(self):
        print('蹲')

    def run(self):
        print('跑')


class fps_player(player):
    def shoot(self):
        print('开火')

xiaoming = fps_player()
xiaoming.jump()
xiaoming.squat()
xiaoming.run()
xiaoming.shoot()
