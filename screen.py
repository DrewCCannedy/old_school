"""Map for the Old_School game."""

from colorama import Fore, Style

from help import get_color_str


class Map:
    def __init__(self, name, data, left=None, right=None, up=None, down=None):
        self.name = name
        self.data = data
        self.left = left
        self.right = right
        self.up = up
        self.down = down


class MapController:
    """Contains maps and functions to update those maps."""
    def __init__(self):
        self.columns = 50
        self.rows = 11

        self.maps = self.create_maps()
        self.current_map = self.maps[2]

    def update(self, player, objects, enemies, pui, wui):
        """Update the map with the players position."""
        if pui:
            self.player_input = pui
        else:
            self.player_input = "You Are Exploring"
        if wui:
            self.world_input = wui
        else:
            self.world_input = "No Enemies"

        # convert the map string to a list in order to do [] insertion
        current_map = list(self.current_map.data)

        # put objects in map
        for o in objects:
            if o.room == self.current_map.name:
                pos = o.x + o.y * self.columns
                current_map[pos] = get_color_str(o.char, 'blue')
        
        # converts the player's x and y to a position of the map string
        player_position = player.x + player.y * self.columns
        
        # only let the player move to an unnocupied space
        if not current_map[player_position] in ' ' + get_color_str('D', 'blue'):
            player.x = player.px
            player.y = player.py
            player_position = player.x + player.y * self.columns
        
        current_map[player_position] = get_color_str('p', "green")

        # put enemies in map
        for o in enemies:
            if o.room == self.current_map.name:
                pos = o.x + o.y * self.columns
                if o.dead:
                    color = "magenta"
                else:
                    color = "red"
                current_map[pos] = get_color_str(o.char, color)

        output = ''.join(current_map)
        # print map, print UI
        print(output, end='')
        print(get_color_str(self.player_input, "green"))
        print(get_color_str(self.world_input, "red"))

    def change(self, direction):
        if direction == 'right':
            next_map = self.current_map.right
        elif direction == 'left':
            next_map = self.current_map.left
        elif direction == 'up':
            next_map = self.current_map.up
        elif direction == 'down':
            next_map = self.current_map.down

        self.current_map = self.find_map(next_map)

    def find_map(self, name):
        for item in self.maps:
            if item.name == name:
                return item

    def delete(self, cord):
        delete_pos = cord[0] + cord[1] * self.columns
        current_map = list(self.current_map.data)
        current_map[delete_pos] = ' '
        map_string = ''
        for item in current_map:
            map_string += item
        index = self.maps.index(self.current_map)
        self.maps[index].data = map_string
        # self.current_map = self.maps[0]

    def create_maps(self):
        maps = []

        map = []
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXX               XXXXX       XXXXXXXXXXXXXX")
        map.append("XXXXXXXXX   XXXXXXXXX   XXXXX       XXXXXXXXXXXXXX")
        map.append("XXXXXXXXX   XXXXXXXXX   XXXXX                     ")
        map.append("X           XXXXXXXXX   XXXXX       XXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXX   XXXXXXXXX   XXXXXXXXXXXXXX")
        map.append("XXX       XXXXX         XXXXXXX     XXXXXXXXXXXXXX")
        map.append("XXXXX                   XXXXX       XXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXX                       XXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map_string = ""
        for item in map:
            map_string += item
        name = "Tutorial 1"
        maps.append(Map(name, map_string, "Janitor's Cave", "Tutorial 2"))

        map = []
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map_string = ""
        for item in map:
            map_string += item
        name = "Tutorial 2"
        maps.append(Map(name, map_string, "Tutorial 1"))

        map = []
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX X XXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXX")
        map.append("                                                  ")
        map.append("                                                  ")
        map.append("                                                  ")
        map.append("                                                  ")
        map.append("XXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXX X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map_string = ""
        for item in map:
            map_string += item
        name = "School Hall"
        maps.append(Map(name, map_string, None, None,
                        "Huff Class", "Janitor's Cave"))

        map = []
        map.append("XXXXXXXXXXXXXXX X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXX               XXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXX               X                         ")
        map.append("XXXXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXX               XXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map_string = ""
        for item in map:
            map_string += item
        name = "Janitor's Cave"
        maps.append(Map(name, map_string, None, "Tutorial 1", "School Hall"))

        map = []
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        map.append("XXXXXXXXXX                                      XX")
        map.append("XXXXXXXXXXXX     k   k   k   k   k           D  XX")
        map.append("XXXXXXXXXXXX     k   k   k   k   k           D  XX")
        map.append("XXXXXXXXXXXX     k   k   k   k   k              XX")
        map.append("XXXXXXXXXXXX                                    XX")
        map.append("XXXXXXXXXX       XXXXXXXXX                      XX")
        map.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXX")
        map_string = ""
        for item in map:
            map_string += item
        name = "Huff Class"
        maps.append(Map(name, map_string, None, None, None, "School Hall"))

        return maps
