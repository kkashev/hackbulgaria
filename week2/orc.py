from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor

    def attack(self):
        return(self.weapon.damage * self.berserk_factor)
