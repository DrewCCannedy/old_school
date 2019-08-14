"""Npc objects for the old school game."""

from game_object import GameObject
from help import get_color_str, getch


class MrsHuff(GameObject):
    """Mrs Huff NPC for old school."""

    def __init__(self, dict_):
        self.skipped_first_interaction = True
        super().__init__(dict_)

    def get_info(self, player):
        gold_star = get_color_str("Gold Star", "yellow")
        if "Tissues" not in player.inventory and "Gold Star" not in player.inventory:
            out_string = "Hey buddy. Can you run to the janitor's closet "
            out_string += "and get us some more tissues? "
            out_string += "I'll give you a {}!".format(gold_star)
            self.skipped_first_interaction = False
        elif "Gold Star" not in player.inventory:
            if not self.skipped_first_interaction:
                out_string = "Great job buddy! "
                out_string += "Here's your {}, ".format(gold_star)
                out_string += "as promised!"
            else:
                out_string = "Are those tissues for me? "
                out_string = "How did you know we needed these? "
                out_string = "You must be an extra special lil punkin. *Teehee*"
                out_string = "Here's a {}!".format(gold_star)
            player.add_inventory("Gold Star")
            player.remove_inventory("Tissues")
        else:
            out_string = "I'm all out of gold stars for today buddy."

        self.description = out_string
        self.get_info_help()
        getch()
