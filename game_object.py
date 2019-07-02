"""Object for the Old_School game."""

from getch import getch
from help import center_align, clear, get_color_str


class GameObject:

    def __init__(self, dict_):
        for key in dict_:
            setattr(self, key, dict_[key])

    def get_info(self, player):
        self.get_info_help()
        getch()

    def get_info_help(self):
        """Prints name and description."""
        spaces = 50 - len(self.name) - 8
        desline = center_align(self.description)
        clear()
        print('\n\n')
        print(' ' * (int(spaces/2)), end='')
        print(self.char + '---', end='')
        print(get_color_str(self.name.upper(), "red"), end='')
        print('---' + self.char, end='')
        print('\n\n' + desline)


class Door(GameObject):

    def __init__(self, dict_):
        super().__init__(dict_)

    def get_info(self, player):
        self.get_info_help()
        out = center_align('Open the door? y/n')
        print('\n' + out)
        player_input = getch()
        clear()
        # action: open door
        if player_input == 'y':
            # only open if they have the key
            if self.key in player.inventory or self.key is None:
                if self.key in player.inventory:
                    des = 'You unlock the door using the {}'.format(get_color_str(self.key, "yellow"))
                else:
                    des = 'The door opens'
                out = des
                _return = self.unlock_cord
            else:
                out = 'The door is locked'
        # action: leave the door
        else:
            out = 'Fearing what is beyond, '
            out += 'you leave the door for another day'
        out = center_align(out)
        print('\n\n\n{}\n\n'.format(out))
        getch()
        if _return:
            return _return

class Chest(GameObject):

    def __init__(self, dict_):
        self.empty = False
        super().__init__(dict_)

    def get_info(self, player):
        self.get_info_help()
        out = center_align('Open this? y/n')
        print('\n' + out)
        player_input = getch()
        # action: open chest
        clear()
        if not self.empty:
            if player_input == 'y':
                out = 'You found a {}'.format(get_color_str(self.treasure, "yellow"))
                player.add_inventory(self.treasure)
                self.empty = True
            else:
                out = 'Fearing the unknown, '
                out += 'you leave it closed for another day'
        else:
            out = 'You find nothing... perhaps someone has already take the contents'
        out = center_align(out)
        print('\n\n\n{}\n\n'.format(out))
        getch()
