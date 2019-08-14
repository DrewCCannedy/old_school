"""An RPG in CMD."""

import os

from pygame import mixer

import player
import screen
from object_manager import ObjectManager
from enemy import EnemyManager
from debug import log
from help import getch

player = player.Player(x=2, y=4, px=2, py=2, health=5, inventory=[])
move_commands = ['d', 'a', 's', 'w']
attack_commands = ['j', 'k', 'l', 'i', 'm']

map = screen.MapController()

enemy_manager = EnemyManager()
object_manager = ObjectManager()

mixer.init()
mixer.Sound("sounds/noodle.wav").play(-1)

playing = True

# set console size
command = 'mode con: cols={} lines={}'.format(map.columns, map.rows+2)
os.system(command)
# player ui, world ui
pui = ""
wui = ""
while playing:
    # updates the map with player pos, all room objects
    # Enemy positions and the player and world UIs
    map.update(player, object_manager.objects, enemy_manager.enemies, pui, wui)
    # enemy actions
    for enemy in enemy_manager.enemies:
        enemy.move()
    try:
        user_input = getch()
    # catches if the user inputs an arrow key or something
    except UnicodeDecodeError as e:
        user_input = ""
        log("Error occured during get_input: {}".format(e))
    # action: quit
    if user_input == 'q':
        playing = False
    # action: move
    elif user_input in move_commands:
        next_room = player.move(user_input)
        # action: change room
        if next_room:
            map.change(next_room)
            player.change_rooms(next_room)
    # action: inspect object
    elif user_input == 'e':
        o = object_manager.search_objects(player)
        if o is None:
            o = enemy_manager.search_enemies(player, map.current_map.name)
        try:
            if o.room == map.current_map.name:
                result = o.get_info(player)
            # if a door is opened
            if result:
                map.delete(result)
        except AttributeError as e:
            log("Error occured during get_info(): {}".format(e))
    # action: inspect player
    elif user_input == 'u':
        player.show_info()
    # action: inspect room
    elif user_input == 'r':
        map.current_map.show_info()
    # action: attack
    elif user_input == "k":
        user_input = getch()
        if user_input in attack_commands:
            current_enemy = enemy_manager.search_enemies(player, map.current_map.name)
            # take in slashes
            if user_input != 'k':
                user_input += getch()
                user_input += getch()
            try:
                pui = current_enemy.take_damage(user_input)
            except AttributeError:
                pass
    # need to attack after player moves
    enemies_present = False
    for enemy in enemy_manager.enemies:
        current_enemy = enemy_manager.search_enemies(player, map.current_map.name)
        if current_enemy == enemy:
            wui = enemy.attack_player(player, map.current_map.name)
        enemy.move_timer += 1
        enemy.check_dead()