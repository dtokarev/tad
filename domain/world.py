import random
import math

from domain import enemy


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
        self.enemy = None
        self.loot = None
        self.generate_enemy()
        self.generate_loot()

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
        if home_distance < 5:
            return 0

        dif = math.ceil(home_distance / 5)
        dif += random.randint(-1, int(dif / 5))

        return int(dif)

    def __str__(self):
        return str(self.get_info())


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




