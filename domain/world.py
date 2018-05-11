import random

import config
from service import enemy_service


class Coordinate:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return "Current position: {}:{}".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


class MapTile:
    def __init__(self, coordinate: Coordinate):
        self.coordinate = coordinate
        self.enemy_difficulty = MapTile.get_enemy_difficulty(coordinate)
        self.enemy = None
        self.loot = None

        if random.random() < 0.7 and (coordinate.x + coordinate.y) > 5:
            self.enemy = enemy_service.generate(self.enemy_difficulty)

    @staticmethod
    def get_actual_difficulty(coordinate: Coordinate) -> int:
        return (abs(coordinate.x) + abs(coordinate.y)) / 10

    @staticmethod
    def get_enemy_difficulty(coordinate: Coordinate) -> int:
        dif = MapTile.get_actual_difficulty(coordinate) + random.randint(-1, 1)
        dif *= config.difficulty

        return int(dif)

    def get_info(self) -> dict:
        return {
            "position": self.coordinate,
            "enemy": self.enemy,
            "difficulty": self.enemy_difficulty,
            "loot": self.loot,
        }


class Map:
    def __init__(self):
        self.initial_coordinate = Coordinate(0, 0)
        self.map = {self.initial_coordinate: MapTile(self.initial_coordinate)}

    def open_tile(self, coordinate: Coordinate):
        if coordinate in self.map:
            return self.map.get(coordinate)

        new_tile = MapTile(coordinate)
        self.map.update({coordinate: new_tile})
        return new_tile

    def get_tile(self, coordinate: Coordinate):
        if coordinate not in self.map:
            return None

        return self.map.get(coordinate)



