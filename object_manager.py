import json

from game_object import GameObject, Door, Chest
from npc import MrsHuff


class ObjectManager:
    """Object manager for old school."""
    def __init__(self):
        self.objects = []
        self.create_objects()

   

    # create objects from the objects.json file
    def create_objects(self):
        path = "json/objects.json"
        f = open(path)

        list_ = json.load(f)
        for dict_ in list_:
            class_name = dict_["class_name"]
            if class_name == "GameObject":
                o = GameObject(dict_)
            elif class_name == "Door":
                o = Door(dict_)
            elif class_name == "Chest":
                o = Chest(dict_)
            elif class_name == "MrsHuff":
                o = MrsHuff(dict_)
            self.objects.append(o)

    # just in case we want to update objects.json
    def write_objects(self):
        path = "json/objects.json"

        f = open(path, 'w')
        dicts = []
        for o in self.objects:
            dicts.append(o.__dict__)
        json.dump(dicts, f)
        f.close()

    def search_objects(self, player):
        for o in self.objects:
            if o.x == player.x:
                if o.y >= player.y - 1 and o.y <= player.y + 1:
                    return o
            elif o.y == player.y:
                if o.x == player.x - 1 or o.x == player.x + 1:
                    return o
        return None
