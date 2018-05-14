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
    _visible_range = 3
    loc = player.get_current_tile().coordinate
    for x in range(loc.x-_visible_range, loc.x+_visible_range+1):
        for y in range(loc.y - _visible_range, loc.y + _visible_range+1):
            repr = player.map.get_tile_representation(loc)
            print("|{}".format(repr), end="")
        print()
        print("-"*_visible_range*2*7, end="")
        print()

