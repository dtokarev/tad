class Item:
    def __init__(self, name: str, desc: str):
        self.desc = desc
        self.name = name


class Weapon(Item):
    def __init__(self, name, desc, damage):
        super().__init__(name, desc)
        self.damage = damage
