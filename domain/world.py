import random
import math

from domain import enemy


class Coordinate:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __hash__(self, *args, **kwargs):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __str__(self):
        return "{}:{}".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


class MapTile:
    def __init__(self, coordinate: Coordinate):
        self.coordinate = coordinate
        self.enemy = None
        self.loot = None
        self.generate_enemy()
        self.generate_loot()
        self.is_visited = False

    def get_info(self) -> dict:
        return {
            "position": self.coordinate,
            "enemy": self.enemy,
            "difficulty": self.get_enemy_difficulty(),
            "loot": self.loot,
        }

    def generate_enemy(self) -> None:
        if random.random() < 0.7:
            self.enemy = enemy.generate(self.get_enemy_difficulty())

    def generate_loot(self):
        pass

    def get_home_distance(self) -> int:
        return abs(self.coordinate.x) + abs(self.coordinate.y)

    def get_enemy_difficulty(self) -> int:
        home_distance = self.get_home_distance()
        if home_distance < 2:
            return 0

        dif = math.ceil(home_distance / 5)
        dif += random.randint(-1, int(dif / 5))

        return int(dif)

    def __str__(self):
        return str(self.get_info())


class Map:
    def __init__(self):
        self.initial_coordinate = Coordinate(0, 0)
        init_tile = MapTile(self.initial_coordinate)
        init_tile.is_visited = True
        self.map = {
            self.initial_coordinate: init_tile
        }

    def open_tile(self, coordinate: Coordinate):
        if coordinate in self.map:
            return self.map.get(coordinate)

        new_tile = MapTile(coordinate)
        self.map.update({coordinate: new_tile})
        return new_tile

    def get_tile(self, coordinate: Coordinate):
        return self.map.get(coordinate)

    def get_tile_representation(self, target_loc: Coordinate, current_loc: Coordinate = None):
        tile = self.get_tile(target_loc)

        if not tile:
            return " ", "\033[0m"
        elif target_loc == current_loc:
            return "O", "\033[01;33m"
        elif tile.enemy:
            return ("E", "\033[00;31m") if tile.enemy.is_alive() else ("D", "\033[01;33m")

        return "_", "\033[01;33m"



