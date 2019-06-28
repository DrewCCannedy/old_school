from game_object import GameObject, Door, Chest
from npc import MrsHuff

import json

class ObjectManager:
    """Object manager for old school."""
    def __init__(self):
        self.objects = []
        self.create_objects()
        self.write_objects()

    def write_objects(self):
        path = "objects.json"

        f = open(path, 'w')
        dicts = []
        for o in self.objects:
            dicts.append(o.__dict__)
        json.dump(dicts, f)
        f.close()

    def create_objects(self):
        # tutorial 1 objects
        des = "It reads: \"Walk the path of those who came before; "
        des += "destroy that which should never have been created\""
        o = GameObject("an old chalkboard", des, 'B', 11, 4, 'Tutorial 1')
        self.objects.append(o)

        des = "Surely you don't plan on returning to that retched place"
        unlock_cord = [0, 4]
        name = "The door back to school"
        o = Door(name, des, 'D', 1, 4, "Tutorial 1",
                 unlock_cord, "Janitor's Key")
        self.objects.append(o)

        des = "It reads: \"A great foe lies ahead;"
        des += " press 'k' to strike him\""
        o = GameObject("an old chalkboard", des, 'B', 23, 1, 'Tutorial 1')
        self.objects.append(o)

        des = "It reads: \"More Challenging Enemies Require Greater Strikes; "
        des += "the next foe will require "
        des += "two strikes, followed by a left slash\""
        o = GameObject("an old chalkboard", des, 'B', 3, 6, 'Tutorial 1')
        self.objects.append(o)

        des = "It reads: \"A great foe lies ahead;"
        des += " press 'jkl' to perform a left slash\""
        o = GameObject("an old chalkboard", des, 'B', 29, 7, 'Tutorial 1')
        self.objects.append(o)

        # tutorial 2 objects
        des = "The wood is old and cracked"
        o = Chest("Wooden Chest", des, 't', 11, 2, 'Tutorial 2',
                  "Janitor's Key")
        self.objects.append(o)

        # school hall objects
        name = "Door to Mrs. Huff's Classroom"
        des = "Your lovely teacher"
        unlock_cord = [32, 1]
        o = Door(name, des, 'D', 32, 2, "School Hall", unlock_cord)
        self.objects.append(o)

        name = "Door to the Janitor's Cave"
        des = "Smells pretty spooky"
        unlock_cord = [16, 8]
        o = Door(name, des, 'D', 16, 7, "School Hall", unlock_cord)
        self.objects.append(o)

        # janitor's closet
        name = "A Strange Door"
        des = "Ever hear about the kid who opened the strange door? "
        des += "Hear he ended up beating the game or something"
        unlock_cord = [24, 4]
        o = Door(name, des, 'D', 23, 4, "Janitor's Cave", unlock_cord)
        self.objects.append(o)

        name = "Door to the Hall"
        des = "What? You don't like brooms and stuff?"
        unlock_cord = [16, 0]
        o = Door(name, des, 'D', 16, 1, "Janitor's Cave",
                 unlock_cord, "Janitor's Key")
        self.objects.append(o)

        des = "What would a kid want with stinky cleaning supplies?"
        o = GameObject("Janitorial Supplies", des,
                       'J', 9, 6, "Janitor's Cave")
        self.objects.append(o)

        des = "The legendary drawer filled with trash"
        o = GameObject("Trash Drawer", des,
                       'T', 23, 2, "Janitor's Cave")
        self.objects.append(o)

        # Huff's Class
        des = "Buzz off. Can't you see I'm busy slimo?"
        o = GameObject("Shelby Blacksmith", des, 'k', 33, 5, "Huff Class")
        self.objects.append(o)

        o = MrsHuff()
        self.objects.append(o)

    def search_objects(self, player):
        for o in self.objects:
            if o.x == player.x:
                if o.y >= player.y - 1 and o.y <= player.y + 1:
                    return o
            elif o.y == player.y:
                if o.x == player.x - 1 or o.x == player.x + 1:
                    return o
        return None
