import random
from typing import Optional


class Enemy:
    def __init__(self):
        self.name = "unknown"
        self.type = "unknown"
        self.health = 100
        self.damage_range = 0, 0

    def __str__(self):
        return self.name

    def get_damage(self) -> int:
        return random.randint(*self.damage_range)

    def get_average_damage(self) -> float:
        return sum(self.damage_range) / 2

    def get_difficulty(self):
        return round(self.health / 10 + self.get_average_damage() / 3, 2)

    def is_alive(self):
        return self.health > 0

    def loot(self):
        pass


class Wolf(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Wolf"
        self.health = 5
        self.damage_range = 2, 3


class Spider(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Spider"
        self.health = 5
        self.damage_range = 2, 5


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "GiantSpider"
        self.health = 8
        self.damage_range = 4, 6


def generate(difficulty: int) -> Optional["Enemy"]:
    enemies = [Wolf(), Spider(), GiantSpider()]

    if difficulty < 1:
        return None

    available = [e for e in enemies if (difficulty + 1) > e.get_difficulty() > (difficulty - 1)]

    return random.sample(available, 1)[0] if available else None

