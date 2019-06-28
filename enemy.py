"""Enemy for the Old_School Game."""

from gameobject import GameObject


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.create_enemies()

    def create_enemies(self):
        o = Oogly(17, 7, 'Tutorial 1', True)
        self.enemies.append(o)

        o = Oogly(5, 6, "Tutorial 1", False)
        self.enemies.append(o)

        o = GreaterOogly(31, 2, 'Tutorial 1', True)
        self.enemies.append(o)

    def search_enemies(self, player, room):
        for o in self.enemies:
            if o.room == room:
                if o.y == player.y:
                    if o.x == player.x - 1 or o.x == player.x + 1:
                        return o


class Enemy(GameObject):
    """Enemy for Old School Game."""

    def __init__(self, name, description, char, x, y,
                 room, health, damage, move):
        GameObject.__init__(self, name, description, char, x, y, room)
        self.health = health
        self.damage = damage
        self.dead = False
        self.move_capable = move
        self.move_timer = 0

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

    def __init__(self, x, y, room, move):
        name: str = "Greater Oogly"
        description: str = "Like an Oogly (but greater)"
        char: str = 'C'
        health: list = ['k', 'k', 'jkl']
        damage: int = 1
        Enemy.__init__(self, name, description, char,
                       x, y, room, health, damage, move)

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

    def __init__(self, x, y, room, move):
        name: str = "An Oogly"
        description: str = "A small misshapen child."
        char: str = 'c'
        health: list = ['k', 'k']
        damage: int = 1
        Enemy.__init__(self, name, description, char,
                       x, y, room, health, damage, move)
