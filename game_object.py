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
        # action: open door
        if player_input == 'y':
            clear()
            # only open if they have the key
            if self.key in player.inventory or self.key is None:
                if self.key in player.inventory:
                    des = 'You unlock the door using the {}'
                else:
                    des = 'The door opens'
                out_string = des.format(self.key)
                out = center_align(out_string)
                print('\n\n\n{}\n\n'.format(out))
                getch()
                return self.unlock_cord
            else:
                out = center_align('The door is locked')
                print('\n\n\n{}\n\n'.format(out))
                getch()
        # action: leave the door
        else:
            clear()
            out = 'Fearing what is beyond, '
            out += 'you leave the door for another day'
            out = center_align(out)
            print('\n\n\n{}\n\n'.format(out))
            getch()


class Chest(GameObject):

    def __init__(self, dict_):
        super().__init__(dict_)

    def get_info(self, player):
        self.get_info_help()
        out = center_align('Open the chest? y/n')
        print('\n' + out)
        player_input = getch()
        # action: open chest
        if player_input == 'y':
            clear()
            out_string = 'You found a {}'.format(self.treasure)
            player.add_inventory(self.treasure)
            out = center_align(out_string)
            print('\n\n\n{}\n\n'.format(out))
            getch()
        else:
            clear()
            out = 'Fearing the unknown, '
            out += 'you leave the chest for another day'
            out = center_align(out)
            print('\n\n\n{}\n\n'.format(out))
            getch()
