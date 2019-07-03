"""Map for the Old_School game."""

import json

from help import get_color_str
from debug import log


class Map:
    def __init__(self, dict_):
        for key in dict_:
            setattr(self, key, dict_[key])


class MapController:
    """Contains maps and functions to update those maps."""
    def __init__(self):
        self.columns = 50
        self.rows = 11

        self.maps = []
        self.create_maps()
        for m in self.maps:
            if m.name == "Tutorial 2":
                self.current_map =  m

    def update(self, player, objects, enemies, pui, wui):
        """Update the map with the players position."""
        if pui:
            self.player_input = pui
        else:
            self.player_input = "You Are Exploring"
        if wui:
            self.world_input = wui
        else:
            self.world_input = "All is well"

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

    # just in case we want to update maps.json
    def write_maps(self):
        path = "json/maps.json"

        f = open(path, 'w')
        dicts = []
        for o in self.maps:
            dicts.append(o.__dict__)
        json.dump(dicts, f)
        f.close()

    def create_maps(self):
        path = "json/maps.json"
        f = open(path)

        list_ = json.load(f)
        for dict_ in list_:
            self.maps.append(Map(dict_))
