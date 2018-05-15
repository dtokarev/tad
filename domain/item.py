class Item:
    def __init__(self, name: str, desc: str):
        self.desc = desc
        self.name = name
        self.rarity = 0
        self.value = 0


class Weapon(Item):
    def __init__(self, name, desc, damage, value):
        super().__init__(name, desc)
        self.value = value
        self.damage = damage


class Consumable(Item):
    pass


class Food(Consumable):
    def __init__(self, name, heal_value):
        super().__init__(name, "food")
        self.heal_value = heal_value
