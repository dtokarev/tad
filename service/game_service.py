from domain.enemy import Enemy
from domain.player import Player
from domain.world import Coordinate


def get_action(message: str) -> str:
    return str(input(message)).lower()


def explore_tile(player: Player):
    print(player.get_current_tile())
    enemy = player.get_current_tile().enemy

    if enemy and enemy.is_alive:
        attack_tile(player, enemy)


def attack_tile(player: Player, enemy: Enemy) -> None:
    while player.is_alive() and enemy.is_alive():
        player_damage = player.get_attack()
        print("Player attacked {} for {} hp".format(enemy.name, player_damage))
        enemy.health -= player_damage

        if not enemy.is_alive():
            break

        enemy_damage = enemy.get_damage()
        print("{} attacked player for {} hp".format(enemy.name, enemy_damage))
        player.health -= enemy_damage

    winner = player if player.is_alive() else enemy
    print("{} won, {} hp left".format(winner.name, winner.health))


def print_nearby_map(player: Player):
    _visible_range = 1
    current_loc = player.get_current_tile().coordinate

    line_last = ""
    for y in range(current_loc.y+_visible_range, current_loc.y-_visible_range-1, -1):
        line1 = ""
        line2 = ""
        for x in range(current_loc.x - _visible_range, current_loc.x + _visible_range+1):
            target_loc = Coordinate(x, y)
            tile_repr = player.map.get_tile_representation(target_loc, current_loc)
            line1 += "|---"
            line2 += "| {} ".format(tile_repr)
        print(line1+"|")
        print(line2+"|")
        line_last = line1
    print(line_last + "|")

