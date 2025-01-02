# sorted
from operator import itemgetter, attrgetter

player_tuple = [("Alice", "Bow", 12), ("Ethan", "Box", 20), ("Sophia", "Staff", 15)]
print(sorted(player_tuple, key=lambda x: x[2]))


class Player:
    def __init__(self, name, weapon, level):
        self.name = name
        self.weapon = weapon
        self.level = level

    def __repr__(self):
        return repr((self.name, self.weapon, self.level))


player_objects = [Player('Alice', 'Bow', 12),
                  Player('Ethan', 'Axe', 20),
                  Player('Sophia', 'Staff', 15)]
print(sorted(player_objects, key=lambda player: player.weapon))

print('使用operator系列')
print(sorted(player_tuple, key=itemgetter(2)))
print(sorted(player_objects, key=attrgetter('level')))
print('使用operator系列,多列排序')
print(sorted(player_tuple, key=itemgetter(0, 1)))
print(sorted(player_tuple, key=lambda x: (x[0], -x[2])))
