from domain.enemy import *


enemies = [Wolf, Spider, GiantSpider]


def generate(difficulty: int) -> "Enemy":
    difficulty = difficulty if difficulty > 1 else 1
    available = [e for e in Enemy.all if (difficulty + 1) > e.get_difficulty() > (difficulty - 1)]

    return random.sample(available)
