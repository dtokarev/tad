from domain.item import Weapon
from domain.world import Map, Coordinate, MapTile


class Player:

    def __init__(self, name, age, favorite_foods):
        self.favorite_foods = favorite_foods
        self.level = 1
        self.health = 100
        self.name = name
        self.age = age
        self.map = Map()
        self.position = self.map.initial_coordinate
        self.weapons = []
        self.food = []
        self.clothes = []
        self.stuff = []

    @staticmethod
    def build():
        player = Player(name="Adam", age=20, favorite_foods=["bread"])
        player.weapons.append(Weapon("dagger", "Old rusty dagger", 5))
        player.stuff = ["item1", "gold(5)"]
        return player

    def print_inventory(self):
        print("Inventory: ")
        for item in self.get_inventory():
            print(item)

    def get_inventory(self):
        return [self.weapons + self.food + self.clothes + self.stuff]

    def get_current_tile(self) -> MapTile:
        return self.map.get_tile(self.position)

    def move(self, dx: int, dy: int) -> None:
        new_coordinate = Coordinate(self.position.x + dx, self.position.y + dy)
        self.map.open_tile(new_coordinate)
        self.position = new_coordinate







