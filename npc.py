"""Npc objects for the old school game."""

from game_object import GameObject
from getch import getch


class MrsHuff(GameObject):
    """Mrs Huff NPC for old school."""

    def __init__(self, dict_):
        super().__init__(dict_)

    def get_info(self, player):
        if "Janitor's Key" not in player.inventory:
            out_string = "Hey buddy. Can you run to the janitor's closet "
            out_string += "and get us some more tissues? "
            out_string += "I'll give you a gold star!"
        elif "Gold Star" not in player.inventory:
            out_string = "Great job buddy! "
            out_string += "Here's your gold star, "
            out_string += "as promised!"
            player.add_inventory("Gold Star")
        else:
            out_string = "I'm all out of gold stars for today buddy."

        self.description = out_string
        self.get_info_help()
        getch()
