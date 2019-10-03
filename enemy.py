"""Enemy for the Old_School Game."""

import json

from game_object import GameObject
from help import log


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.create_enemies()

    # create enemies from the enemies.json file
    def create_enemies(self):
        path = "json/enemies.json"
        f = open(path)

        list_ = json.load(f)
        for dict_ in list_:
            class_name = dict_["class_name"]
            if class_name == "Oogly":
                o = Oogly(dict_)
            elif class_name == "BigBrudder":
                o = BigBrudder(dict_)
            elif class_name == "HeartBreaker":
                o = HeartBreaker(dict_)
            self.enemies.append(o)


    def search_enemies(self, player, room):
        for o in self.enemies:
            if o.room == room:
                if o.in_range(player):
                    return o

    # just in case we want to update the enemies.json
    def write_enemies(self):
        path = "json/enemies.json"

        f = open(path)
        dicts = []
        for o in self.enemies:
            dicts.append(o.__dict__)
        json.dump(dicts, f)
        f.close()


class Enemy(GameObject):
    """Enemy for Old School Game."""

    def __init__(self):
        self.dead = False
        self.move_capable = True
        self.move_timer = True
        self.x_attack_range = 1
        self.y_attack_range = 0

    def attack_player(self, player, room):
        if not self.dead:
            if self.move_timer % 2 == 0 or not self.move_capable:
                return self.attack(player)

    def in_range(self, player):
        for cord in range(0, self.y_attack_range + 1):
            if self.y == player.y + cord or self.y == player.y - cord:
                for cord in range(1, self.x_attack_range * 2):
                    if self.x == player.x - cord or self.x == player.x + cord:
                        return True
        return False

    def attack(self, player):
        player.take_damage(self.damage)
        return "You took {} damage from {}".format(self.damage, self.name)

    def take_damage(self, attack):
        if attack in self.health:
            self.health.remove(attack)
            if len(self.health) == 0:
                return "You killed {}".format(self.name)
            else:
                return "You struck {}".format(self.name)
        else:
            return "That didn't seem to effect {}".format(self.name)

    def check_dead(self):
        if len(self.health) == 0:
            self.dead = True


class BigBrudder(Enemy):
    """First Complex Enemy in Old School."""

    def __init__(self, dict_):
        super().__init__()
        self.name = "Big Brudder"
        self.description =  "A child, fat and bloated with no discernable facial features."
        self.char = "B"
        self.health = [
            "k",
            "k",
            "jkl"
        ]
        self.damage = 1
        for key in dict_:
            setattr(self, key, dict_[key])

    def move(self):
        if not self.dead:
            if self.move_capable:
                if self.move_timer == 1:
                    self.x += 2
                elif self.move_timer == 3:
                    self.y += 1
                elif self.move_timer == 5:
                    self.x -= 2
                elif self.move_timer == 7:
                    self.move_timer = -1
                    self.y -= 1


class Oogly(Enemy):
    """Most common enemy in Old School."""

    def __init__(self, dict_):
        super().__init__()
        self.name = "Oogly"
        self.description =  "A small misshapen child."
        self.char = "o"
        self.health = [
            "k",
            "k",
        ]
        self.damage = 1
        for key in dict_:
            setattr(self, key, dict_[key])
    
    def move(self):
        if not self.dead:
            if self.move_capable:
                if not self.move_timer % 2 == 0:
                    if self.move_timer == 1:
                        self.x += 2
                    elif self.move_timer == 3:
                        self.move_timer = -1
                        self.x -= 2


class HeartBreaker(Enemy):
    """First Boss."""

    def __init__(self, dict_):
        super().__init__()
        self.name = "Heart Breaker"
        self.description = "A popular kid in a previous life, now a hollow shell of skin and bones."
        self.char = "H"
        self.x_attack_range = 2
        self.y_attack_range = 1
        self.health = [
            "jkl",
            "lkj",
        ]
        self.damage = 1
        for key in dict_:
            setattr(self, key, dict_[key])

    def move(self):
        if not self.dead:
            if self.move_capable:
                if not self.move_timer % 2 == 0:
                    if self.move_timer < 14:
                        self.x += 2
                    elif self.move_timer < 27:
                        self.x -= 2
                    else:
                        self.x -=2
                        self.move_timer = -1
