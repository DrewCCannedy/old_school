"""Enemy for the Old_School Game."""

from game_object import GameObject
import json


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
            elif class_name == "GreaterOogly":
                o = GreaterOogly(dict_)
            self.enemies.append(o)


    def search_enemies(self, player, room):
        for o in self.enemies:
            if o.room == room:
                if o.y == player.y:
                    if o.x == player.x - 1 or o.x == player.x + 1:
                        return o

    # just in case we want to update the enemies.json
    def write_enemies(self):
        path = "enemies.json"

        f = open(path)
        dicts = []
        for o in self.enemies:
            dicts.append(o.__dict__)
        json.dump(dicts, f)
        f.close()


class Enemy(GameObject):
    """Enemy for Old School Game."""

    def run(self, player, room):
        # action: die
        if len(self.health) == 0:
            self.dead = True
        if not self.dead:
            # action: attack
            result = self.attack_player(player, room)
            # action: move
            self.move()
            # action: attack
            if result is None:
                result = self.attack_player(player, room)
            return result

    def attack_player(self, player, room):
        if self.room == room:
            if self.x == player.x:
                if self.y == player.y - 1 or self.y == player.y + 1:
                    return self.attack(player)
            elif self.y == player.y:
                if self.x == player.x - 1 or self.x == player.x + 1:
                    return self.attack(player)

    def move(self):
        if self.move_capable:
            if self.move_timer == 1:
                self.x += 2
            elif self.move_timer == 3:
                self.move_timer = -1
                self.x -= 2
            self.move_timer += 1

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


class GreaterOogly(Enemy):
    """First Complex Enemy in Old SChool."""

    def __init__(self, dict_):
        for key in dict_:
            setattr(self, key, dict_[key])

    def move(self):
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
            self.move_timer += 1


class Oogly(Enemy):
    """Most common enemy in Old School."""

    def __init__(self, dict_):
        for key in dict_:
            setattr(self, key, dict_[key])
