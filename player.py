"""Player for the Old_School Game."""
from dataclasses import dataclass, field

from help import clear, center_align, get_color_str, getch


@dataclass
class Player:
    """Class for the Player object in Old School"""
    # x, y position
    x: int = 2
    y: int = 4
    # previous x, y position
    px: int = 2
    py: int = 4
    health: int = 5
    inventory: list = field(default_factory=list)

    def change_rooms(self, direction):
        if direction == 'right':
            self.x = 2
        elif direction == 'left':
            self.x = 48
        elif direction == 'up':
            self.y = 8
        elif direction == 'down':
            self.y = 1

    def move(self, input):
        x_move_speed = 2
        y_move_speed = 1

        self.py = self.y
        self.px = self.x

        if input == 'a':
            if self.x > 0:
                self.x -= x_move_speed
            else:
                return "left"
        if input == 'd':
            if self.x < 48:
                self.x += x_move_speed
            else:
                return "right"
        if input == 'w':
            if self.y > 0:
                self.y -= y_move_speed
            else:
                return "up"
        if input == 's':
            if self.y < 9:
                self.y += y_move_speed
            else:
                return "down"

        return False

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        #TODO: impliment death
        pass

    def add_inventory(self, item):
        self.inventory.append(item)

    def remove_inventory(self, item):
        self.inventory.remove(item)

    def show_info(self):
        clear()
        print()
        des = center_align("HEALTH: {}".format(self.health))
        print(des)
        des = center_align("INVENTORY")
        print(des)

        # print inventory
        if len(self.inventory) == 0:
            print(center_align("empty"))
        inv = "--"
        for item in self.inventory:
            inv += item + "--"
        des = center_align(inv)
        print(des)
        getch()
