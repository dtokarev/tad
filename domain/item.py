class Item:
    def __init__(self, name: str, desc: str):
        self.desc = desc
        self.name = name


class Weapon(Item):
    def __init__(self, name, desc, damage):
        super().__init__(name, desc)
        self.damage = damage


class Gold(Item):
    def __init__(self):
        super().__init__("Gold", "basic currency")


class Consumable(Item):
    pass


class Food(Consumable):
    def __init__(self, name, heal_value):
        super().__init__(name, "food")
        self.heal_value = heal_value
