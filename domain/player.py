from domain.item import Weapon, Food
from domain.world import Map, Coordinate, MapTile


class Player:
    MAX_HEALTH = 100

    def __init__(self, name, age):
        self.level = 1
        self.health = Player.MAX_HEALTH
        self.name = name
        self.age = age
        self.map = Map()
        self.position = self.map.initial_coordinate
        self.weapons = []
        self.food = []
        self.clothes = []
        self.stuff = []

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

    def get_attack(self) -> int:
        damage = sum(float(w.damage) for w in self.weapons)

        return int(damage)

    def is_alive(self):
        return self.health > 0


def build():
    player = Player(name="Adam", age=20)
    player.weapons.append(Weapon("dagger", "Old rusty dagger", 1))
    for i in range(5):
        player.food.append(Food("Bread", 5))
    player.stuff = ["item1", "gold(5)"]
    return player






